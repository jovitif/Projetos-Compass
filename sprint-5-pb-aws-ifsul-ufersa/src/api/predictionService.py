import pandas as pd
from Reservation import Reservation

class PredictionService:
    def __init__(self, modelo_treinado):             # Construtor do service que sera inciado com o caminho do modelo treinado
        self.model = modelo_treinado

    def predict_price(self, reservation_data):
        try:
            reservation = Reservation(**reservation_data) # Inicializar um objeto com base em um dicionário
            features = pd.DataFrame({   # Mapeamento por meio do DataFrame
                "no_of_adults": [reservation.no_of_adults],
                "no_of_weekend_nights": [reservation.no_of_weekend_nights],
                "no_of_week_nights": [reservation.no_of_week_nights],
                "type_of_meal_plan": [reservation.type_of_meal_plan],
                "room_type_reserved": [reservation.room_type_reserved],
                "lead_time": [reservation.lead_time],
                "market_segment_type": [reservation.market_segment_type],
                "no_of_special_requests": [reservation.no_of_special_requests],
                "booking_status": [reservation.booking_status],
                "arrival_year": [reservation.arrival_year],
                "arrival_month": [reservation.arrival_month],
                "arrival_date": [reservation.arrival_date]
            })

            prediction = self.model.predict(features)    # Faz a previsão usando o modelo carregado (self.model)
            result = {"result": int(prediction[0] + 1)}  # Calcula o resultado da previsão
            return result
        except Exception as e:
            return {"error": f"Erro ao fazer a previsão: {str(e)}"}, 400
