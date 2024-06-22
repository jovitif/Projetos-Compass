import json
from json.decoder import JSONDecodeError
import boto3
from datetime import datetime, timezone
from utils.utils import valid_img, object_exists, check_input, dog_races


def v2_vision(event):
    try:
        request = json.loads(event.get('body'))
        reqBucket = request.get('bucket')
        reqImageName = request.get('imageName')


        #verifica se os slots não estão vazios
        input_check_result = check_input(reqBucket, reqImageName)
        if input_check_result:
            return {
                "statusCode": 500,
                "body": json.dumps({"error": input_check_result})
            }


        # Verifica se o nome da imagem é válido utilizando a função do utils
        if not valid_img(reqImageName):
            response = {
                "statusCode": 500,
                "body": json.dumps({"error": "Formato da imagem inválida"})
            }
            return response

        #verifica se a imagem existe e guarda a data de criação dela
        try:
            created_image_time = object_exists(reqImageName, reqBucket)
            if not created_image_time:
                response = {"statusCode" : 500, "body" : "erro ao acessar a imagem"}
                return response
        except:
            response = {"statusCode" : 500, "body" : "erro ao acessar a imagem"}
            return response


        #cria o client do rekognition
        client = boto3.client('rekognition')
        rekognitionResponse = client.detect_labels(
            Image={
                'S3Object':
                {
                    'Bucket' : reqBucket,
                    'Name' : reqImageName
                }
            },
            MinConfidence = 90.0,
            Features = ["GENERAL_LABELS"],
            Settings = {
                "GeneralLabels" :
                    {
                        "LabelCategoryInclusionFilters" : ["Animals and Pets"]
                    }
            },
        )
        print(rekognitionResponse)


        labels = rekognitionResponse['Labels']

        #formata as labels para a saida
        labels_formatted = [
            {"Confidence": label['Confidence'], "Name": label['Name'] }
            for label in labels
                if True
        ]

        #busca a raça do animal
        race = [label['Name'] for label in labels_formatted if label['Name'] in dog_races]

        #verifica se o labels_formatted tem mais do que 4 labels
        if(len(labels_formatted) > 4):
            raceDict = [
                {'Confidence' : label['Confidence'], 'Name' : label['Name']}
                for label in labels_formatted
                if label['Name'] in dog_races
            ]
            raceFound = False
            for i in range(3):
                if labels_formatted[i]['Name'] == race:
                    raceFound = True
                    break
            if not raceFound and len(raceDict) != 0:
                labels_formatted[3] = raceDict[0]

            del labels_formatted[4:]

        # importando o serviço do bedrock
        debrock_runtime = boto3.client(service_name='bedrock-runtime')

        # pegando cada caracteristica identificada no atributo Name
        caracteristicas = set()

        for label in labels_formatted:
            caracteristicas.add(label.get('Name'))

        # prompt digitado para ser usado no serviço do bedrock
        prompt_digitado = f'''
        Contexto: Tenho animal com as seguintes caracteristicas {caracteristicas}

        Exemplo:
        Dicas sobre Labradores:
        Nível de Energia e Necessidades de Exercícios: ().
        Temperamento e Comportamento: ().
        Cuidados e Necessidades: ().
        Problemas de Saúde Comuns: ().

        Objetivo: coloque as informações acimas como no exemplo anterior substituindo todas as informações de labradores pela raça identificada

        '''

        # Corpo de uma requisição HTTP feita no serviço do bedrock
        request_body = json.dumps({
            'inputText': prompt_digitado,
            'textGenerationConfig':{
                'maxTokenCount': 4096,
                'stopSequences':[],
                'temperature':0,
                'topP':0.9
            }
        })

        # Modelo utilizado para a geração das dicas
        modelId = 'amazon.titan-text-express-v1'
        accept = "application/json"
        contentType = "application/json"
        generatedText = '\n'

        # Gerando dicas
        model_response = debrock_runtime.invoke_model(body=request_body, modelId=modelId, accept=accept, contentType=contentType)
        response_contents = json.loads(model_response.get("body").read().decode('utf-8'))
        generatedText = response_contents.get('results')[0].get('outputText')
        dica = generatedText[generatedText.index('\n')+1:]

        urlToImage = f"https://{reqBucket}.s3.amazonaws.com/{reqImageName}"

        dica = generatedText.replace('\n', ' ')

        # json gerado quando uma imagem é identificada com a url, data de criação, labels e dicas
        body = {
            "url_to_image": urlToImage,
            "created_image": created_image_time,
            "labels": labels_formatted,
            "Dicas": dica
        }


        response = {"statusCode" : 200, "body" : json.dumps(body)}
        return response

    #caso de algum erro durante o tratamento dos dados vai para o except
    except(TypeError, JSONDecodeError):
         response = {"statusCode": 500, "body": "Requisição inválida "}
