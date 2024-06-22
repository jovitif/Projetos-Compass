import json
import re

pattern = re.compile(r"(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}")
horarios = ['manhã', 'tarde']
exames = ['raio_x', 'espirometria', 'audiometria', 'acuidade_visual']
servicos = ['atendimento_clínico', 'outros_exames']

def validate_aso(slots):
    # Validar horario
    if not slots['horario']:
        print('Validando slot Horario')

        return {
            'isValid': False,
            'invalidSlot': 'horario'
        }

    if slots['horario']['value']['originalValue'].lower().strip() not in horarios:
        print('Horário inválido!')

        return {
            'isValid': False,
            'invalidSlot': 'horario',
            'message': 'Por favor, selecione um desses horários: ({}).'.format(", ".join(horarios))
        }
        
    # Validar nome
    if not slots['nome']:
        print('Validando slot Nome')

        return {
            'isValid': False,
            'invalidSlot': 'nome'
        }
        
    # Validar número de contato
    if not slots['contato']:
        print('Validando slot Contato')
    
        return {
            'isValid': False,
            'invalidSlot': 'contato'
        }
    
    if not validate_phone_number(pattern, slots['contato']['value']['originalValue']):
        print('Número inválido!')
        
        return {
            'isValid': False,
            'invalidSlot': 'contato',
            'message': 'Por favor, confira o seu número está correto.'
        }
        

    # Entrada válida
    return {'isValid': True}

def validate_exam(slots):
    # Validar exames
    if not slots['exame']:
        print('Validando slot Exames')

        return {
            'isValid': False,
            'invalidSlot': 'exame'
        }
    
    if slots['exame']['value']['originalValue'].lower() not in exames:
        print('Exame inválido!')

        return {
            'isValid': False,
            'invalidSlot': 'exame',
            'message': 'Por favor, selecione um desses exames: ({}).'.format(", ".join(exames))
        }

    # Valid Order
    return {'isValid': True}

def validate_service(slots):
    # Validar serviço
    if not slots['servico']:
        print('Validando slot Servico')

        return {
            'isValid': False,
            'invalidSlot': 'servico'
        }

    if slots['servico']['value']['originalValue'].lower().strip() not in servicos:
        print('Serviço inválido!')

        return {
            'isValid': False,
            'invalidSlot': 'servico',
            'message': 'Por favor, selecione um desses serviços: ({}).'.format(", ".join(servicos))
        }
        
    # Valid Order
    return {'isValid': True}



def validate_phone_number(regex, phone_number):
    match = re.search(regex, phone_number)
    return match