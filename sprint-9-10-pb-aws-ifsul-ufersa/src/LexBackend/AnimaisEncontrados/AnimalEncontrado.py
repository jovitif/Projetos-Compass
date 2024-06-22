from Utils import ResponseMessage, ResponseNoMessage, ValidateSlots
import boto3
import json



def AnimalEncontradoFunc(event):
    
    bot = event['bot']['name']
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    session_attributes = event['sessionState']['sessionAttributes']

    validation = ValidateSlots(slots, intent)
    
    if 'bedrockText' not in session_attributes:
        session_attributes['bedrockText'] = []
    
    if event['interpretations'][0]['intent']['confirmationState'] == "Confirmed":
        #enviar para o lambda responsável por guardar no dynamo
        lambdaClient = boto3.client('lambda')
        functionName = 'lostanimals-dev-dynamoController'

        response = lambdaClient.invoke(
        FunctionName= functionName,
        InvocationType='Event',
        Payload=json.dumps(event)
        )
        response = ResponseNoMessage(intent, slots, "Delegate", "", session_attributes)
    else:
        if 'bedrock' in validation:
            print("entrou no validation")
            session_attributes['bedrockText'] = validation['bedrock']
        if not validation['isValid']:
            if 'message' in validation:
                response = ResponseMessage(intent, slots, "ElicitSlot", validation['message'], validation['invalidSlot'], session_attributes)
            else:
                response = ResponseNoMessage(intent, slots, "ElicitSlot", validation['invalidSlot'], session_attributes)
        else:
            print("passou")
            response = ResponseNoMessage(intent, slots, "Delegate", "", session_attributes)

    
    return response