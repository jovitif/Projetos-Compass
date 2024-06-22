import boto3
import os

def RekognitionController(s3FileKey, context):
  BucketName = os.environ['BUCKET_NAME']
  print(s3FileKey)
  #verifica se a chamada vem do controlador do dynamo ou do controlador de imagem
  flag = False
  if s3FileKey.startswith("https://lostanimalsphotos.s3.amazonaws.com/"):
    s3FileKey = s3FileKey.replace("https://lostanimalsphotos.s3.amazonaws.com/", "")
    flag = True
    print(s3FileKey)

  rekognitionClient = boto3.client('rekognition')
  rekognitionResponse = rekognitionClient.detect_labels(
            Image={
                'S3Object':
                {
                    'Bucket' : BucketName,
                    'Name' : s3FileKey
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
  labels = rekognitionResponse['Labels']
  labels_formatted = []
  if len(labels) > 0:
    labels_formatted = [
              label['Name']
              for label in labels
                  if True
          ]
  print("labels")
  print(labels)
  if flag:
    print(labels_formatted)
    return labels_formatted
  else:
    if 'Animal' in labels_formatted:
      url_to_image = f'https://{BucketName}.s3.amazonaws.com/{s3FileKey}'
      print(url_to_image)
      response = url_to_image
    else:
      response = 'noImage'

  return response