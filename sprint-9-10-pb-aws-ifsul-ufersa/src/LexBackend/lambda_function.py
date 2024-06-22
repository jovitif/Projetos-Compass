from AnimaisPerdidos.AnimalPerdido import AnimalPerdidoFunc
from AnimaisEncontrados.AnimalEncontrado import AnimalEncontradoFunc

import json

def lambda_handler(event, context):
    
    bot = event['bot']['name']
    slots = event['sessionState']['intent']['slots']
    intent = event['sessionState']['intent']['name']
    
    response = {}
    print(event)
    
    if event['invocationSource'] == 'DialogCodeHook':
        
        if intent == 'AnimalPerdido':
            #redireciona para a função do animal perdido
            response = AnimalPerdidoFunc(event)
        elif intent == 'AnimalEncontrado':
            #redireciona para a função do animal encontrado
            response = AnimalEncontradoFunc(event)
        
    

    return response