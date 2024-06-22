import json
import boto3
import unicodedata

def BedrockController(event, context):

  observacao = event['observacao']
  #caracteristicas = event['labels']
  localizacao = event['local']
  
  prompt_digitado = f'''
        Você receberá uma localização que o animal foi visto e uma observação do usuário. Por favor, use essas informações para descrever um animal perdido de maneira clara e detalhada, para ajudar na busca.

        
### Características detectadas pelo Rekognition:
- Última localização conhecida: {localizacao}

### Observação do usuário:
{observacao}

Baseado nas informações acima, forneça uma descrição breve do animal perdido, A descrição deve ser organizada e fácil de entender, comente apenas sobre os dados fornecidos.

        '''

  request_body = json.dumps({
    'inputText': prompt_digitado,
    'textGenerationConfig':{
      'maxTokenCount': 4096,
      'stopSequences':[],
      'temperature':0.2,
      'topP':0.9
    }
  })

  modelId = 'amazon.titan-text-express-v1'
  accept = "application/json"
  contentType = "application/json"
  generatedText = '\n'

  bedrock_runtime = boto3.client(service_name='bedrock-runtime')

  model_response = bedrock_runtime.invoke_model(
    body=request_body, 
    modelId=modelId, 
    accept=accept, 
    contentType=contentType)

  response_contents = json.loads(model_response.get("body").read().decode('utf-8'))

  generatedText = response_contents.get('results')[0].get('outputText')

  generatedText = ''.join(c for c in unicodedata.normalize('NFD', generatedText) if not unicodedata.combining(c))
  generatedTextFormat = generatedText.replace(".", "")

  return generatedTextFormat