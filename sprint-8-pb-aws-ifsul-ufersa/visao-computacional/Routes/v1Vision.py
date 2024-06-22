import json
import boto3
from datetime import datetime
from utils.utils import valid_img, object_exists, check_input

def analyze_image(bucket, imageName):
    # Inicializa o cliente Rekognition
    rekognition = boto3.client('rekognition')

    # Chama o serviço Rekognition para analisar a imagem
    response = rekognition.detect_faces(
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': imageName
            }
        },
        Attributes=['ALL']
    )

    print(response)

    return response

def extract_emotion(face_details_list):
    emotions = []
    for face_details in face_details_list:
        if not face_details:
            emotions.append((None, None))
        else:
            # Ordena as emoções detectadas pela confiança
            emotions_sorted = sorted(face_details['Emotions'], key=lambda x: x['Confidence'], reverse=True)
            # Retorna a emoção com maior confiança
            emotions.append((emotions_sorted[0]['Type'], emotions_sorted[0]['Confidence']))

    print(emotions)

    return emotions

def v1_vision(event):
    # Extrai os parâmetros da requisição
    body = json.loads(event['body'])
    bucket = body['bucket']
    imageName = body['imageName']

    # Verifica se o nome da imagem é válido utilizando a função do utils
    if not valid_img(imageName):
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Formato da imagem inválida"})
        }

    # Verifica se o nome do bucket e o nome da imagem foram fornecidos corretamente
    input_check_result = check_input(bucket, imageName)
    if input_check_result:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": input_check_result})
        }

    # Verifica se a imagem existe no S3
    if not object_exists(imageName, bucket):
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Imagem não encontrada no S3"})
        }

    # Analisa a imagem utilizando o serviço Rekognition
    response = analyze_image(bucket, imageName)

    # Extrai as principais emoções 
    emotions = extract_emotion(response.get('FaceDetails', []))
    
    # Monta a resposta da API
    now = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    response_body = {
        "url_to_image": f"https://{bucket}/{imageName}",
        "created_image": now,
        "faces": [],
    }

    # Adiciona as emoções detectadas à resposta
    if emotions:
        for emotion, confidence in emotions:
            if response['FaceDetails']:  # Verifica se há detalhes de rosto disponíveis
                face_detail = response['FaceDetails'][emotions.index((emotion, confidence))]
                response_body['faces'].append({
                    "position": {
                        "Height": face_detail['BoundingBox']['Height'],
                        "Left": face_detail['BoundingBox']['Left'],
                        "Top": face_detail['BoundingBox']['Top'],
                        "Width": face_detail['BoundingBox']['Width']
                    },
                    "classified_emotion": emotion,
                    "classified_emotion_confidence": confidence
                })
    else:
        # Se não houver rostos detectados
        response_body['faces'].append({
            "position": {
                "Height": None,
                "Left": None,
                "Top": None,
                "Width": None
            },
            "classified_emotion": None,
            "classified_emotion_confidence": None
        })

    # Registra a resposta no CloudWatch
    print(response_body)

    # Retorna a resposta da API
    return {
        "statusCode": 200,
        "body": json.dumps(response_body)
    }
