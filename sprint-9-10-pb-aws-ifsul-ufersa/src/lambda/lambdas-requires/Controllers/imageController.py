import requests
import boto3
import os
import json
from datetime import datetime


def ImageController(event):
  print("image")
  print(event)
  bucketName = os.environ['BUCKET_NAME']
  account_sid = os.environ['TWILIO_SID']  
  auth_token = os.environ['TWILIO_AUTH']    
  twilioImageUrl = event['MediaUrl0']

  response = requests.get(twilioImageUrl, auth=(account_sid, auth_token))
  print("essa e a response")
  print(response)
  lexSession = LexGetSession(event['WaId'])
  sessionState = lexSession['sessionState']['intent']['name']
  if sessionState == 'AnimalEncontrado':
    animalType = 'encontrados'
  else:
    animalType = 'perdidos'
  
  uniqueIdentifier = datetime.utcnow().strftime('%Y%m%d%H%M%S%f')


  s3Client = boto3.client('s3')
  if event['MediaContentType0'] == 'image/jpeg':
    s3FileKey = f"{animalType}/{uniqueIdentifier}.jpeg"
  elif event['MediaContentType0'] == 'image/jpg':
    s3FileKey = f"{animalType}/{uniqueIdentifier}.jpg"
  elif event['MediaContentType0'] == 'image/png':
    s3FileKey = f"{animalType}/{uniqueIdentifier}.png"
  
  s3Client.put_object(Bucket=bucketName, Key=s3FileKey, Body=response.content)
  
  # Imagem com acesso público
  s3Client.put_object_acl(ACL='public-read', Bucket=bucketName, Key=s3FileKey)
  
  # Informação da url do áudio
  url_to_image = f'https://{bucketName}.s3.amazonaws.com/{s3FileKey}'
  print("imagem colocada no s3")
  print(url_to_image)

  lambdaClient = boto3.client('lambda')
  functionName = 'lostanimals-dev-rekognitionController'
  response = lambdaClient.invoke(
      FunctionName= functionName,
      InvocationType='RequestResponse',
      Payload=json.dumps(s3FileKey)
  )
  responsePayload = json.load(response['Payload'])
  return responsePayload

def LexGetSession(session):
  client = boto3.client("lexv2-runtime")

  bot_id = os.environ['BOT_ID']
  bot_alias_id = os.environ['BOT_ALIAS']
  locale_id = 'pt_BR'
  session_id = session


  response = client.get_session(
    botId=bot_id,
    botAliasId=bot_alias_id,
    localeId=locale_id,
    sessionId=session_id
      )
  
  print("lexSession")
  print(response)
  return response