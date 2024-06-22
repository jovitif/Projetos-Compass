import json
import boto3
import tempfile
from contextlib import closing
from datetime import datetime
import hashlib
import hmac

import os

BUCKET_NAME = os.getenv(
'BUCKET_NAME'
)
TBL_NAME= os.getenv(
'TBL_NAME'
)

def health(event, context):
    body = {
        "message": "Go Serverless v3.0! Your function executed successfully!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v1_description(event, context):
    body = {
        "message": "TTS api version 1."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v2_description(event, context):
    body = {
        "message": "TTS api version 2."
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response

def v3_description(event, context):

    body = json.loads(event.get('body'))
    phrase = body.get('phrase')
    
    if phrase is None:
        body = {"error": "Erro ao informar o texto"}
        return {"statusCode": 400, "body": json.dumps(body)}
    else:
      audio = phrase.split()
      nome_audio = f'audio-{audio[0]}'
    polly = boto3.client('polly')

    result = polly.synthesize_speech(
        Text=phrase,
        VoiceId='Vitoria',
        OutputFormat='mp3'
    )

    if "AudioStream" in result:
        s3 = boto3.client('s3')
        object_key = f'{nome_audio}.mp3'
        try:
            s3.put_object(
                Bucket=BUCKET_NAME,
                Key=object_key,
                Body=result['AudioStream'].read()
            )
            audio_url = f'https://{BUCKET_NAME}.s3.amazonaws.com/{object_key}'

            body = {
                "received_phrase": phrase,
                "url_to_audio": audio_url,
                "created_audio": datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
            return {"statusCode": 200, "body": json.dumps(body)}
        except Exception as e:
            body = {"error": str(e)}
            return {"statusCode": 500, "body": json.dumps(body)}
    else:
        body = {"error": "Erro ao processar audio"}
        return {"statusCode": 400, "body": json.dumps(body)}

def gerarid(text):
    # Gerar um ID único a partir da frase recebida
    hashed = hashlib.sha256(text.encode()).hexdigest()
    return hashed

def v4_description(event, context):
    try:
        # Recebe o texto do corpo da solicitação
        request_body = json.loads(event['body'])
        text_to_convert = request_body['phrase']

        # Configuração do cliente Polly e S3
        polly_client = boto3.client('polly')
        s3_client = boto3.client('s3')
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(TBL_NAME)

        # Converte o texto em áudio usando o serviço Polly
        response = polly_client.synthesize_speech(
            Text=text_to_convert,
            OutputFormat='mp3',
            VoiceId='Vitoria'
        )

        # Gera um hash para o texto para servir como ID
        text_hash = gerarid(text_to_convert)

        # Define a chave do objeto no bucket S3
        s3_key = f'{text_hash}.mp3'

        # Salva o áudio no bucket S3
        s3_client.put_object(
            Body=response['AudioStream'].read(),
            Bucket=BUCKET_NAME,
            Key=s3_key,
            ContentType='audio/mpeg'
        )

        # Adiciona os detalhes ao DynamoDB
        table.put_item(
            Item={
                'id': text_hash,
                'received_phrase': text_to_convert,
                'url_to_audio': f'https://{BUCKET_NAME}.s3.us-east-1.amazonaws.com/{s3_key}',
                            'created_audio': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            }
        )

        # Prepara a resposta para o usuário
        response_body = {
            'id': text_hash,
            'received_phrase': text_to_convert,
            'created_audio': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
            'url_to_audio': f'https://{BUCKET_NAME}.s3.us-east-1.amazonaws.com/{s3_key}'
        }

        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"{str(e)}, {TBL_NAME}"
        }


def v5_description(event, context):
    try:
        # Recebe o texto do corpo da solicitação
        request_body = json.loads(event['body'])
        text_to_convert = request_body['phrase']

        # Gera um hash para a frase
        text_hash = gerarid(text_to_convert)

        # Configuração do cliente DynamoDB
        dynamodb = boto3.resource('dynamodb')
        table = dynamodb.Table(TBL_NAME)

        # Verifica se o hash existe no DynamoDB
        response = table.get_item(
            Key={
                'id': text_hash
            }
        )

        if 'Item' in response:
            # Se o registro existir, retorna o item encontrado
            return {
                'statusCode': 200,
                'body': json.dumps(response['Item'])
            }
        else:
            # Configuração do cliente Polly e S3
            polly_client = boto3.client('polly')
            s3_client = boto3.client('s3')

            # Converte o texto em áudio usando o serviço Polly
            polly_response = polly_client.synthesize_speech(
                Text=text_to_convert,
                OutputFormat='mp3',
                VoiceId='Vitoria'
            )

            # Define a chave do objeto no bucket S3
            s3_key = f'{text_hash}.mp3'

            # Salva o áudio no bucket S3
            s3_client.put_object(
                Body=polly_response['AudioStream'].read(),
                Bucket=BUCKET_NAME,
                Key=s3_key,
                ContentType='audio/mpeg'
            )

            # Adiciona os detalhes ao DynamoDB
            table.put_item(
                Item={
                    'id': text_hash,
                    'received_phrase': text_to_convert,
                    'url_to_audio': f'https://{BUCKET_NAME}.s3.us-east-1.amazonaws.com/{s3_key}',
                    'created_audio': datetime.now().strftime('%d-%m-%Y %H:%M:%S')
                }
            )

            # Prepara a resposta para o usuário
            response_body = {
                'id': text_hash,
                'received_phrase': text_to_convert,
                'created_audio': datetime.now().strftime('%d-%m-%Y %H:%M:%S'),
                'url_to_audio': f'https://{BUCKET_NAME}.s3.us-east-1.amazonaws.com/{s3_key}'
            }

            return {
                'statusCode': 200,
                'body': json.dumps(response_body)
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }
