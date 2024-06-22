import json

opcoes = ['agendarconsulta', 'cadastramento', 'medicinadotrabalho', 'info']

def validate_initial(slots):
    # Validar interação inicial
    if not slots['opcao']:
        print('Validando slot Opção')

        return {
            'isValid': False,
            'invalidSlot': 'opcao'
        }

    if slots['opcao']['value']['originalValue'].lower().strip() not in opcoes:
        print('Opção inválida!')

        return {
            'isValid': False,
            'invalidSlot': 'opcao',
            'message': 'Por favor, selecione uma dessas opções: ({}).'.format(", ".join(opcoes))
        }
    return {"isValid": True}