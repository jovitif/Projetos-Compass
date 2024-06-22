import base64
import json
import boto3
from urllib.parse import unquote_plus

def connector(event, context):
  if event.get('isBase64Encoded', False):
    body_decoded = base64.b64decode(event['body']).decode('utf-8')
  else:
    body_decoded = event['body']

  bodyJson = dict(
    param.split('=',1) for param in body_decoded.split('&')
  )
  bodyJson = {key: unquote_plus(value) for key, value in bodyJson.items()}
  print(bodyJson)
  # enviando o json para o orquestrador
  lambdaClient = boto3.client('lambda')

  functionName = 'lostanimals-requirements-dev-orchestrator'

  #efetivamente invoca o orquestrador e aguarda a resposta
  response = lambdaClient.invoke(
    FunctionName= functionName,
    InvocationType='RequestResponse',
    Payload=json.dumps(bodyJson)
  )

  responsePayload = json.load(response['Payload'])
  print(responsePayload)

  return {
    'statusCode': 200,
    'body': responsePayload
  }

  