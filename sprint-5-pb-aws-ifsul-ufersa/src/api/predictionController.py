from flask import request, jsonify
from predictionService import PredictionService
import boto3
from io import BytesIO
import joblib

class PredictionController:
    def __init__(self):         # Ira chamar o service e também passar o caminho do modelo treinado
        self.prediction_service = PredictionService(model)

    def predict(self):                      # Método criado para realizar a previsão
        if request.method == 'POST':        # Quando a requisição for do tipo POST
            data = request.json             # Recebe o JSON como argumento
            prediction = self.prediction_service.predict_price(data)
            return jsonify(prediction)      # Retorno da saida com o result
        else:
            return jsonify({"error": "Método POST não permitido"}), 405


# função para ler um modelo do s3
def read_joblib(path):

    # Verifica se path é um bucket s3
    if path[:5] == 's3://':
        s3_bucket, s3_key = path.split('/')[2], path.split('/')[3:]
        s3_key = '/'.join(s3_key)
        with BytesIO() as f:
            boto3.client("s3").download_fileobj(Bucket=s3_bucket, Key=s3_key, Fileobj=f)
            f.seek(0)
            file = joblib.load(f)
    
    # para o caso de path ser um arquivo local
    else:
        with open(path, 'rb') as f:
            file = joblib.load(f)
    
    return file


# pega o modelo do s3 e faz a inferência
model = read_joblib('s3://sprint-5-equipe-2/model.joblib')