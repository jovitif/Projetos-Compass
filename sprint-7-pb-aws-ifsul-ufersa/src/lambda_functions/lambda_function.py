import json
import re
import lambda_agendar_consulta
import lambda_medicina_trabalho
import lambda_cadastro
import lambda_initial_interaction


def lambda_handler(event, context):
    print(event)

    bot = event['bot']['name']
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    
    # Verifica intent para a verificação
    if (intent == 'consulta-aso'):
        order_validation_result = lambda_medicina_trabalho.validate_aso(slots)
    if (intent == 'outros-exames'):
        order_validation_result = lambda_medicina_trabalho.validate_exam(slots) 
    if (intent == 'medicina-do-trabalho'):
        order_validation_result = lambda_medicina_trabalho.validate_service(slots)
    if (intent == 'Cadastramento'):
        order_validation_result = lambda_cadastro.validate_cadastro(slots,event)
    if (intent == 'AgendarConsulta'):
        order_validation_result = lambda_agendar_consulta.validate_order(slots,event)    
    if (intent == 'IniciarInteracao'):
        order_validation_result = lambda_initial_interaction.validate_initial(slots)

    if event['invocationSource'] == 'DialogCodeHook':
        if not order_validation_result['isValid']:
            if 'message' in order_validation_result:
                response = {
                    "sessionState": {
                        "dialogAction": {
                            "slotToElicit": order_validation_result['invalidSlot'],
                            "type": "ElicitSlot"
                        },
                        "intent": {
                            "name": intent,
                            "slots": slots
                        }
                    },
                    "messages": [
                        {
                            "contentType": "PlainText",
                            "content": order_validation_result['message']
                        }
                    ]
                }
            else:
                response = {
                    "sessionState": {
                        "dialogAction": {
                            "slotToElicit": order_validation_result['invalidSlot'],
                            "type": "ElicitSlot"
                        },
                        "intent": {
                            "name": intent,
                            "slots": slots
                        }
                    }
                }
        else:
            response = {
                "sessionState": {
                    "dialogAction": {
                        "type": "Delegate"
                    },
                    "intent": {
                        'name': intent,
                        'slots': slots
                    }
                }
            }

    if event['invocationSource'] == 'FulfillmentCodeHook':
        response = {
            "sessionState": {
                "dialogAction": {
                    "type": "Close"
                },
                "intent": {
                    "name": intent,
                    "slots": slots,
                    "state": "Fulfilled"
                }

            },
            "messages": [
                {
                    "contentType": "PlainText",
                    "content": "Agendamento Concluído."
                }
            ]
        }

    print(response)
    return response