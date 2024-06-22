import os
import json
import boto3
from Controllers.imageController import ImageController
from Controllers.audioController import AudioController

def Orchestrator(event, context):
  print(event)
  if event['MessageType'] == 'text':
    print("texto")
    response = LexRuntime(event['WaId'], event['Body'])
  elif event['MessageType'] == 'image':
    #trata com rekognition
    print("imagem")

    functionResponse = ImageController(event)

    print(functionResponse)
    response = LexRuntime(event['WaId'], functionResponse)
  elif event['MessageType'] == 'audio':
    #trata com o describe 
    print("audio")

    functionResponse = AudioController(event)

    print(functionResponse)

    response = functionResponse
  return response


def LexRuntime(session, message):
  bot_id = os.environ['BOT_ID']
  bot_alias_id = os.environ['BOT_ALIAS']
  locale_id = 'pt_BR'
  session_id = session
  text = message

  try:
    client = boto3.client("lexv2-runtime")

    response = client.recognize_text(
      botId=bot_id,
      botAliasId=bot_alias_id,
      localeId=locale_id,
      sessionId=session_id,
      text=text
      )

    messages = response.get('messages',[])
    print(messages)
    lex_response = messages[0]['content'] if messages else 'no lex response'
    print(lex_response)
    return lex_response
  except Exception as e:
    print("erro: ", e)
    return e
  

