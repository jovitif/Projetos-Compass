import re
import json

pattern = re.compile(r'^\d{3}\.\d{3}\.\d{3}-\d{2}$')

def validate_cadastro(slots,event):    
        def validate_cpf(regex, cpf):
            match = re.search(regex, cpf)
            return match
    
    
    
    
        if not slots['nomeCadastro']:
            print('Validando nome')
            return {
                'isValid': False,
                'invalidSlot': 'nomeCadastro',
                "message": "Qaul o seu nome?"
            }
    
        if not slots['sobrenome']:
            print('Validando sobrenome')
            return {
                'isValid': False,
                'invalidSlot': 'sobrenome'
            }
    
        if not slots['email']:
            print('Validando email')
            return {
                'isValid': False,
                'invalidSlot': 'email'
            }
    
        if not slots['sexo']:
            print('Validando sexo')
            return {
                'isValid': False,
                'invalidSlot': 'sexo'
            }
    
        if not slots['nascimento']:
            print('Validando nascimento')
            return {
                'isValid': False,
                'invalidSlot': 'nascimento'
            }
    
        if not slots['estadoCadastro']:
            print('Validando estadoCadastro')
            return {
                'isValid': False,
                'invalidSlot': 'estadoCadastro'
            }
    
        if not slots['cidadeCadastro']:
            print('Validando cidadeCadastro')
            return {
                'isValid': False,
                'invalidSlot': 'cidadeCadastro'
            }
    
        if not slots['endereco']:
            print('Validando endereco')
            return {
                'isValid': False,
                'invalidSlot': 'endereco',
            }
     # Validar número de contato
        if not slots['cpf']:
            print('Validando cpf')
            return {
                'isValid': False,
                'invalidSlot': 'cpf'
            }
    
        if not validate_cpf(pattern, slots['cpf']['value']['originalValue']):
            print('cpf inválido!')
            return {
                'isValid': False,
                'invalidSlot': 'cpf',
                'message': 'Por favor, confira o seu cpf está correto.'
            }
    
        return {"isValid": True}
    
