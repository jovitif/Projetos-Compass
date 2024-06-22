import boto3
import json

def BedrockCaller(slots, intent):
    
    #imageUrl = slots['FotoDoAnimal']['value']['originalValue']
    endereco = slots['Endereco']['value']['interpretedValue']
    
    '''
    lambdaClient = boto3.client('lambda')
    functionName = 'lostanimals-dev-rekognitionController'
    response = lambdaClient.invoke(
        FunctionName= functionName,
        InvocationType='RequestResponse',
        Payload=json.dumps(imageUrl)
    )
    labels = json.load(response['Payload'])
    print(labels)
    '''
    if intent == 'AnimalEncontrado':
        if slots['InformarObeservacao']['value']['interpretedValue'] == 'sim':
            observacao = slots['Observacao']['value']['interpretedValue']
        else:
            observacao = None
    else:
        observacao = slots['Observacao']['value']['interpretedValue']
        
        
    
    body = {
    "observacao": observacao,
    "local":endereco
    }
    
    lambdaClient = boto3.client('lambda')
    functionName = 'lostanimals-dev-bedrockController'
    responseBedrock = lambdaClient.invoke(
        FunctionName= functionName,
        InvocationType='RequestResponse',
        Payload=json.dumps(body)
    )
    bedrockText = json.load(responseBedrock['Payload'])
    
    
    response = {
        'bedrockText': bedrockText
    }
    
    return response