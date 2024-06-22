import re
import json
from bedrockCaller import BedrockCaller
 
regexEndereco = r"\b(?:avenida|rua)\b.*\b(?:numero|num|proximo)\b|\b(?:numero|num|proximo)\b.*\b(?:avenida|rua)\b"
regexObersevacao = r"^.+$"
def ResponseMessage(intent, slots, dialogType, message, elicitSlot, session):
    if type(session['bedrockText']) == str:
        session['bedrockText'] = json.loads(session['bedrockText'])
    if elicitSlot == "":
        response = {
                    "sessionState": {
                        "dialogAction": {
                            "type": dialogType
                        },
                        "intent": {
                            "name": intent,
                            "slots": slots
                        },
                        "sessionAttributes": {
                            "bedrockText": json.dumps(session['bedrockText'])
                        }
                    },
                    "messages": [
                        {
                            "contentType": "PlainText",
                            "content": message
                        }
                    ]
                }
    else:
        response = {
                    "sessionState": {
                        "dialogAction": {
                            "slotToElicit": elicitSlot,
                            "type": dialogType
                        },
                        "intent": {
                            "name": intent,
                            "slots": slots
                        },
                        "sessionAttributes": {
                            "bedrockText": json.dumps(session['bedrockText'])
                        }
                    },
                    "messages": [
                        {
                            "contentType": "PlainText",
                            "content": message
                        }
                    ]
                }
    return response

    
def ResponseNoMessage(intent, slots, dialogType, elicitSlot, session):
    if type(session['bedrockText']) == str:
        session['bedrockText'] = json.loads(session['bedrockText'])
    if elicitSlot == "":
        response = {
                    "sessionState": {
                        "dialogAction": {
                            "type": dialogType
                        },
                    "sessionAttributes": {
                        "bedrockText": json.dumps(session['bedrockText'])
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
                            "slotToElicit": elicitSlot,
                            "type": dialogType
                        },
                    "sessionAttributes": {
                        "bedrockText": json.dumps(session['bedrockText'])
                    },
                        "intent": {
                            "name": intent,
                            "slots": slots
                        }
                    }
                }
    return response

    
def ValidateSlots(slots, intent):
    
    if not slots['FotoDoAnimal']:
        print('Validando o slot Foto Do Animal')

        return {
            'isValid': False,
            'invalidSlot': 'FotoDoAnimal'
        }

    if not slots['FotoDoAnimal']['value']['originalValue'].lower().startswith("https://lostanimalsphotos.s3.amazonaws.com/"):
        print('Foto Do Animal inválida')
        print(slots['FotoDoAnimal']['value']['originalValue'].lower())
        return {
            'isValid': False,
            'invalidSlot': 'FotoDoAnimal',
            'message': 'por favor envie outra imagem do animal'
        }
    
    if not slots['Endereco']:
        print('Validando o slot endereco')

        return {
            'isValid': False,
            'invalidSlot': 'Endereco'
        }

    if not re.search(regexEndereco, slots['Endereco']['value']['originalValue'].lower(), re.IGNORECASE):
        print('tipo de endereco inválido')
        print(slots['Endereco']['value']['originalValue'].lower())

        return {
            'isValid': False,
            'invalidSlot': 'Endereco',
            'message': 'por favor digite um endereco valido por exemplo: "rua uruguaiana numero 137"'
        }
    
    if intent == "AnimalEncontrado":
        if not slots['InformarTelefone']:
            print('Validando o slot de Informar o Telefone')
    
            return {
                'isValid': False,
                'invalidSlot': 'InformarTelefone'
            }
        
        if slots['InformarTelefone']['value']['originalValue'].lower() not in ['sim', 'nao']:
            print('Informar o Telefone inválido')
    
            return {
                'isValid': False,
                'invalidSlot': 'InformarTelefone',
                'message': 'por favor selecione se deseja Informar o Telefone ou nao'
            }
        
        if not slots['InformarObeservacao']:
            print('Validando o slot de Informar a Obeservacao')
    
            return {
                'isValid': False,
                'invalidSlot': 'InformarObeservacao'
            }
        
        if slots['InformarObeservacao']['value']['originalValue'].lower() not in ['sim', 'nao']:
            print('Informar a Obeservacao inválido')
    
            return {
                'isValid': False,
                'invalidSlot': 'InformarObeservacao',
                'message': 'por favor selecione se deseja Informar uma Obeservacao ou nao'
            }
          
        if slots['InformarObeservacao']['value']['originalValue'].lower() == 'sim':
            if not slots['Observacao']:
                print('Validando o slot Observacao')
                
                return {
                    'isValid': False,
                    'invalidSlot': 'Observacao'
                }
            
            if not re.match(regexObersevacao, slots['Observacao']['value']['originalValue'].lower()):
                print('Observacao inválido')
                
                return {
                    'isValid': False,
                    'invalidSlot': 'Observacao',
                    'message': 'Por favor digite algo sobre a observacao'
                }
        
        if not slots['ConfirmarBedrock']:
            print('Validando o slot do bedrock')
            
            sessionAtt = BedrockCaller(slots, intent)
            print(sessionAtt)
            message = f'Nós geramos a seguinte observação mais detalhada apartir dos seus dados:"{sessionAtt['bedrockText']}" você gostaria que ela fosse adicionada ao registro do animal ? caso opte por não adicionar será usado a sua observação anterior'

            
            return {
                'isValid': False,
                'invalidSlot': 'ConfirmarBedrock',
                'message': message,
                'bedrock':json.dumps(sessionAtt['bedrockText'])
            }
        
        if slots['ConfirmarBedrock']['value']['originalValue'].lower() not in ['sim', 'nao']:
            print('Informar o bedrock')
            
            return {
                'isValid': False,
                'invalidSlot': 'ConfirmarBedrock',
                'message': 'por favor selecione se deseja aceitar esta Obeservacao ou nao'
            }
        
    elif intent == "AnimalPerdido":
        
        
        if not slots['Observacao']:
            print('Validando o slot Observacao')
            
            return {
                'isValid': False,
                'invalidSlot': 'Observacao'
            }

        if not re.match(regexObersevacao, slots['Observacao']['value']['originalValue'].lower()):
            print('Observacao inválido')
            
            return {
                'isValid': False,
                'invalidSlot': 'Observacao',
                'message': 'Por favor digite algo sobre a observacao'
            }
            
        if not slots['ConfirmarBedrock']:
            print('Validando o slot do bedrock')
            
            sessionAtt = BedrockCaller(slots, intent)
            print(sessionAtt)
            message = f'Nós geramos a seguinte observação mais detalhada apartir dos seus dados:"{sessionAtt['bedrockText']}" você gostaria que ela fosse adicionada ao registro do animal ? caso opte por não adicionar será usado a sua observação anterior'

            
            return {
                'isValid': False,
                'invalidSlot': 'ConfirmarBedrock',
                'message': message,
                'bedrock':json.dumps(sessionAtt['bedrockText'])
            }
        
        if slots['ConfirmarBedrock']['value']['originalValue'].lower() not in ['sim', 'nao']:
            print('Informar o bedrock')
            
            return {
                'isValid': False,
                'invalidSlot': 'ConfirmarBedrock',
                'message': 'por favor selecione se deseja aceitar esta Obeservacao ou nao'
            }
        
        if not slots['NomeDoAnimal']:
            print('Validando o slot NomeDoAnimal')
    
            return {
                'isValid': False,
                'invalidSlot': 'NomeDoAnimal'
            }
    
        if not re.match(regexObersevacao, slots['NomeDoAnimal']['value']['originalValue'].lower()):
            print('Nome Do Animal inválido')
    
            return {
                'isValid': False,
                'invalidSlot': 'NomeDoAnimal',
                'message': 'Por favor digite algo sobre o Nome Do Animal'
            }
        
        
        
    
    return {'isValid': True}