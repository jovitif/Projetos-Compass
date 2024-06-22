import boto3
import os
import json
import time
import unicodedata
from twilio.rest import Client

def TranscribeController(event, context):
  bucketName = os.environ['BUCKET_NAME']
  account_sid = os.environ['TWILIO_SID']  
  auth_token = os.environ['TWILIO_AUTH']    
  print("entrou no controlador")
  print(event)
  uniqueIdentifier = event['uniqueIdentifier']
  s3FileKey = f"audios/{uniqueIdentifier}.ogg"
  
  transcribeClient = boto3.client('transcribe')
  transcribeOutputKey = f"audios/transcripts/{uniqueIdentifier}.json"
  response = transcribeClient.start_transcription_job(
    TranscriptionJobName=uniqueIdentifier,
    LanguageCode='pt-BR',  # Defina o idioma do áudio
    MediaFormat='ogg',     # Especifique o formato do áudio
    Media={
        'MediaFileUri': f's3://{bucketName}/{s3FileKey}'
    },
    OutputBucketName=bucketName,
    OutputKey=transcribeOutputKey
  )

    # Obtenha o ID do trabalho de transcrição
  transcription_job_name = response['TranscriptionJob']['TranscriptionJobName']

  # Espere até que o trabalho de transcrição seja concluído
  while True:
      status = transcribeClient.get_transcription_job(TranscriptionJobName=transcription_job_name)
      if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
          break
      print(status)
      time.sleep(1)
  print("completed")
  print(status)
  # Se o trabalho for bem-sucedido, obtenha a transcrição
  if status['TranscriptionJob']['TranscriptionJobStatus'] == 'COMPLETED':
      
      transcription_url = status['TranscriptionJob']['Transcript']['TranscriptFileUri']
      
      # Baixe a transcrição
      response = boto3.client('s3').get_object(Bucket=bucketName, Key=transcribeOutputKey)
      transcript = response['Body'].read().decode('utf-8')

      print("Transcrição:")
      print(transcript)

      transcription_data = json.loads(transcript)

      print(transcription_data['results']['transcripts'][0]['transcript'])

      audioTranscripted = transcription_data['results']['transcripts'][0]['transcript']
      
      #remove os ascentos da frase
      audioTranscripted = ''.join(c for c in unicodedata.normalize('NFD', audioTranscripted) if not unicodedata.combining(c))
      transcriptFormattedToLex = audioTranscripted.replace(".", "")

      dictToLex = {
          'MessageType':'text',
          'WaId':event['WaId'],
          'Body':transcriptFormattedToLex
      }
      #envia para o lex para receber a resposta necessária
      lambdaClient = boto3.client('lambda')
      functionName = 'lostanimals-requirements-dev-orchestrator'
      response = lambdaClient.invoke(
          FunctionName= functionName,
          InvocationType='RequestResponse',
          Payload=json.dumps(dictToLex)
      )
      responsePayload = json.load(response['Payload'])
      print(responsePayload)

      twilioClient = Client(account_sid, auth_token)
      message = twilioClient.messages.create(
        body=responsePayload,
        from_=event['To'],
        to = event['From']
      )
      print(message)
  else:
      print("O trabalho de transcrição falhou.")