import requests
import boto3
import os
import json
import time
from datetime import datetime
import unicodedata

def AudioController(event):
  bucketName = os.environ['BUCKET_NAME']
  account_sid = os.environ['TWILIO_SID']  
  auth_token = os.environ['TWILIO_AUTH']    
  twilioAudioUrl = event['MediaUrl0']
  print("audio")

  responseTwilio = requests.get(twilioAudioUrl, auth=(account_sid, auth_token))
  
  uniqueIdentifier = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
  print(responseTwilio)
  s3Client = boto3.client('s3')
  s3FileKey = f"audios/{uniqueIdentifier}.ogg"

  s3Client.put_object(Bucket=bucketName, Key=s3FileKey, Body=responseTwilio.content)
  
  # audio com acesso público
  s3Client.put_object_acl(ACL='public-read', Bucket=bucketName, Key=s3FileKey)
  
  # Informação da url do áudio
  url_to_audio = f'https://{bucketName}.s3.amazonaws.com/{s3FileKey}'
  print("audio colocada no s3")
  print(url_to_audio)
  

  event['uniqueIdentifier'] = uniqueIdentifier

  # envia para o transcribe fazer o processamento do audio
  lambdaClient = boto3.client('lambda')
  functionName = 'lostanimals-requirements-dev-transcribeController'
  response = lambdaClient.invoke(
      FunctionName= functionName,
      InvocationType='Event',
      Payload=json.dumps(event)
  )
  print("mandou")
  textToTwilio = 'Seu audio está sendo processado...'
  return textToTwilio

