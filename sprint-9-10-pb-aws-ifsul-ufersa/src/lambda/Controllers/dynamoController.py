import json
import boto3
from datetime import datetime, timedelta, timezone

def DynamoController(event, context):
  print(event)
  lexResponse = event

  imageUrl = lexResponse['interpretations'][0]['intent']['slots']['FotoDoAnimal']['value']['originalValue']
  endereco = lexResponse['interpretations'][0]['intent']['slots']['Endereco']['value']['interpretedValue']
  
  gmt_minus_3 = timezone(timedelta(hours=-3))
  now_utc = datetime.now(timezone.utc)
  now_brasilia = now_utc.astimezone(gmt_minus_3)
  formatted_date_time = now_brasilia.strftime('%d/%m/%Y %H:%M')

  lambdaClient = boto3.client('lambda')
  functionName = 'lostanimals-dev-rekognitionController'
  response = lambdaClient.invoke(
      FunctionName= functionName,
      InvocationType='RequestResponse',
      Payload=json.dumps(imageUrl)
  )
  labels = json.load(response['Payload'])
  print(labels)

  if lexResponse['interpretations'][0]['intent']['name'] == 'AnimalEncontrado':
    print("encontrado")
    categoria = 'encontrado'
    if lexResponse['interpretations'][0]['intent']['slots']['InformarTelefone']['value']['interpretedValue'] == 'sim':
      telefone = lexResponse['sessionId']
    else:
      telefone = None
    
    if lexResponse['interpretations'][0]['intent']['slots']['InformarObeservacao']['value']['interpretedValue'] == 'sim':
      observacao = lexResponse['interpretations'][0]['intent']['slots']['Observacao']['value']['interpretedValue']
    else:
      observacao = None

  elif lexResponse['interpretations'][0]['intent']['name'] == 'AnimalPerdido':
    print("perdido")
    categoria = 'perdido'
    telefone = lexResponse['sessionId']  
    observacao = lexResponse['interpretations'][0]['intent']['slots']['Observacao']['value']['interpretedValue']
    nomeDoAnimal = lexResponse['interpretations'][0]['intent']['slots']['NomeDoAnimal']['value']['interpretedValue']
    
  if lexResponse['interpretations'][0]['intent']['slots']['ConfirmarBedrock']['value']['interpretedValue'] == 'sim':
    bedrockText = lexResponse['sessionState']['sessionAttributes']['bedrockText']
  else:
    bedrockText = observacao

  dynamoDB = boto3.client('dynamodb')

  flag = False

  itemKey = {'imageurl':{'S': imageUrl}}
  # verifica se o item não existe na tabela
  try:
    response = dynamoDB.get_item(
      TableName = 'lostAnimalsTable',
      Key = itemKey
    )
    if 'Item' in response:
      flag = True
  except Exception as e:
    print('erro ao consultar no dynamo: ')
    print(e)

  characteristicsList = []
  for label in labels:
    characteristicsList.append({"S": label})
  
  if not flag:
    if categoria == "encontrado":
      dynamoBody = {
        'imageurl': {"S": imageUrl},
        'categoria': { "S": categoria},
        'endereco':{"S": endereco},
        'telefone':{"S": str(telefone)},
        'observacao':{"S": bedrockText},
        'data':{'S': formatted_date_time},
        'caracteristicas':{"L": characteristicsList}
      }
      dynamoDB.put_item(
        TableName='lostAnimalsTable',
        Item=dynamoBody
      )
    else:
      dynamoBody = {
        'imageurl': {"S": imageUrl},
        'categoria': { "S": categoria},
        'endereco':{"S": endereco},
        'telefone':{"S": telefone},
        'observacao':{"S": bedrockText},
        'data':{'S': formatted_date_time},
        'caracteristicas':{"L": characteristicsList},
        'nomedoanimal':{"S": nomeDoAnimal}
      }
      dynamoDB.put_item(
        TableName='lostAnimalsTable',
        Item=dynamoBody
      )