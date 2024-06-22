import json
import re
import datetime

especialidades = ['cardiologista', 'pediatra', 'ortopedista', 'otorrinolaringologista', 'medico do trabalho', 'ginecologista']
horario_inicio = datetime.time(9, 0)
horario_fim = datetime.time(20, 0)


def validate_order(slots,event):
    
     # Validar Estado
   
    if not slots['Estado']:
        print('Validando estado')
        return {
                'isValid': False,
                'invalidSlot': 'Estado',
                
            }
            
    # Validar CidadesDisponiveisRs
   
    if "RS" in slots['Estado']['value']['resolvedValues']:
        if not slots['CidadesDisponiveisRs']:
            print('Validando CidadesDisponiveisRs')
            return {
                    'isValid': False,
                    'invalidSlot': 'CidadesDisponiveisRs',
                    
                }        
        if slots['CidadesDisponiveisRs']['value']['resolvedValues']:
            cidade_slot = event['sessionState']['intent']['slots']['CidadesDisponiveisRs']
            slots['Cidade'] = cidade_slot
            slots['CidadesDisponiveisSp'] = {
                'value': {
                    'originalValue': 'null',
                    'resolvedValues': ['null'],
                    'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
            
            slots['CidadesDisponiveisPr'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
            
            slots['CidadesDisponiveisSc'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
        else:  return {
                    'isValid': False,
                    'invalidSlot': 'CidadesDisponiveisRs',
                    
                }            

    # Validar CidadesDisponiveisSp
    
    if "SP" in slots['Estado']['value']['resolvedValues']:
        if not slots['CidadesDisponiveisSp']:
            print('Validando CidadesDisponiveisSp')
            return {
                    'isValid': False,
                    'invalidSlot': 'CidadesDisponiveisSp',
                    
                }        
        if slots['CidadesDisponiveisSp']['value']['resolvedValues']:
            cidade_slot = event['sessionState']['intent']['slots']['CidadesDisponiveisSp']
            slots['Cidade'] = cidade_slot
            slots['CidadesDisponiveisRs'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
            
            slots['CidadesDisponiveisPr'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
            
            slots['CidadesDisponiveisSc'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
        else:  return {
                    'isValid': False,
                    'invalidSlot': 'CidadesDisponiveisSp',
                    
                }            
            
    # Validar CidadesDisponiveisPr
    
    if "PR" in slots['Estado']['value']['resolvedValues']:
        if not slots['CidadesDisponiveisPr']:
            print('Validando CidadesDisponiveisPr')
            return {
                    'isValid': False,
                    'invalidSlot': 'CidadesDisponiveisPr',
                    
                }        
        if slots['CidadesDisponiveisPr']['value']['resolvedValues']:
            cidade_slot = event['sessionState']['intent']['slots']['CidadesDisponiveisPr']
            slots['Cidade'] = cidade_slot
            slots['CidadesDisponiveisRs'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
            
            slots['CidadesDisponiveisSp'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
            
            slots['CidadesDisponiveisSc'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
        else:  return {
                    'isValid': False,
                    'invalidSlot': 'CidadesDisponiveisPr',
                    
                }            
    
    # Validar CidadesDisponiveisSc       
    
    if "SC" in slots['Estado']['value']['resolvedValues']:
        if not slots['CidadesDisponiveisSc']:
            print('Validando CidadesDisponiveisSc')
            return {
                    'isValid': False,
                    'invalidSlot': 'CidadesDisponiveisSc',
                    
                }        
        if slots['CidadesDisponiveisSc']['value']['resolvedValues']:
            cidade_slot = event['sessionState']['intent']['slots']['CidadesDisponiveisSc']
            slots['Cidade'] = cidade_slot
            slots['CidadesDisponiveisRs'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
            
            slots['CidadesDisponiveisSp'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
            
            slots['CidadesDisponiveisPr'] = {
            'value': {
                'originalValue': 'null',
                'resolvedValues': ['null'],
                'interpretedValue': 'null'
                },
                'shape': 'Scalar'
            }
        else:  return {
                    'isValid': False,
                    'invalidSlot': 'CidadesDisponiveisSc',
                    
                }        
   # Validar cidade
    #cidade_slot = event['sessionState']['intent']['slots']['Cidade']
    if not slots['Cidade'] :
        print('Validando cidade')
        return {
                'isValid': False,
                'invalidSlot': 'Cidade',
                
            }
            
    print('VALOOOOORRRRRR de cidade_slot:', cidade_slot)
   

    # Validar especialidade
    if not slots['especialidade']:
        print('Validando especialidade')

        return {
            'isValid': False,
            'invalidSlot': 'especialidade'
        }

    if slots['especialidade']['value']['originalValue'].lower() not in especialidades:
        print('Especialidade não oferecida.')

        return {
            'isValid': False,
            'invalidSlot': 'especialidade'
        }
    
    # Validar data
    if not slots['DataAgendamento']:
        print('Validando data')

        return {
            'isValid': False,
            'invalidSlot': 'DataAgendamento'
        }

    # Validar horário de atendimento

    if not slots['HorarioAgendamento']:
        print('Validando Horario de Agendamento ')

        return {
            'isValid': False,
            'invalidSlot': 'HorarioAgendamento'
        }
    else:
        #Captura horário selecionado pelo usuário
        horario_agendamento_str = slots['HorarioAgendamento']['value']['interpretedValue']
        horario_agendamento = datetime.datetime.strptime(horario_agendamento_str, "%H:%M").time()
        if   horario_agendamento < horario_inicio or horario_agendamento > horario_fim:
            print('Horário indisponível, por favor, escolha um horário entre 9:00 e 20:00')

            return {
                'isValid': False,
                'invalidSlot': 'HorarioAgendamento',
                'message': 'Horário indisponível, por favor, escolha um horário entre 9:00 e 20:00'
            }

    

    # Valid Order
    return {'isValid': True}
