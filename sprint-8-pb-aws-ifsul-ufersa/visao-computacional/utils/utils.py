import boto3
from botocore.exceptions import ClientError

dog_races = ['Labrador Retriever', 'Bulldog', 'Golden Retriever', 'German Shepherd', 'Husky', 'Beagle', 'Poodle', 'Chihuahua', 'Chow', 'Collie', 'Pitbull']

# vereficação da existencia da imagem no S3
def object_exists(img_name, bucket):
    s3 = boto3.client('s3')

    try:
         # obtendo metadados do objeto do S3
        response = s3.head_object(Bucket=bucket, Key=img_name)

       # Extraindo a data de criação do objeto dos metadados
        creation_date = response['LastModified'].strftime("%d-%m-%Y %H:%M:%S")
        
        return creation_date
    except s3.exceptions.ClientError as e:
        # verifica se é um erro de "NotFound" 
        if e.response['Error']['Code'] == '404':
            return False
        else:
            raise 

# validação do formato de imagem
def valid_img(img_name):
    img_name_lower = img_name.lower()
    if img_name_lower.endswith('.png') or img_name_lower.endswith('.jpg') or img_name_lower.endswith('.jpeg'):
        return True
    else:
        return False
    
def check_input(bucket, img_name):
    if not bucket or not img_name:
        return "Bucket ou nome da imagem nao fornecidos."
    else:
        return None  # Retorna None se ambos os valores forem fornecidos corretamente
