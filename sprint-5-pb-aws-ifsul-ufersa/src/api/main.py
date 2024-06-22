from flask import Flask, jsonify
from predictionController import PredictionController

class MainApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.prediction_controller = PredictionController()

        @self.app.route('/') # apenas uma rota de teste para ver o funcionamento
        def home():
            return 'API em funcionamento'

        @self.app.route('/api/v1/predict', methods=['GET'])    # Quando a requisição for do tipo GET
        def check_model():
            from predictionService import model
            if model:
                return jsonify({"status": "Modelo está carregado e pronto para previsões"})
            else:
                return jsonify({"status": "Modelo não está carregado"}), 500

        @self.app.route('/api/v1/predict', methods=['POST'])   # Quando a requisição for do tipo POST executar para realizar a previsão
        def predict():
            return self.prediction_controller.predict()

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    main_app = MainApp()
    main_app.run()
