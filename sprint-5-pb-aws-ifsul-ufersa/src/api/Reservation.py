# Classe usada para simular uma entidade da Reserva
class Reservation:
    def __init__(self, no_of_adults, no_of_weekend_nights, no_of_week_nights,
                 type_of_meal_plan, room_type_reserved, lead_time,
                 market_segment_type, no_of_special_requests, booking_status,
                 arrival_year, arrival_month, arrival_date):
        # Construtor padrão com seus atributos da classe
        self.no_of_adults = no_of_adults  # Número de adultos na reserva
        self.no_of_weekend_nights = no_of_weekend_nights  # Número de noites de fim de semana na reserva
        self.no_of_week_nights = no_of_week_nights  # Número de noites durante a semana na reserva
        self.type_of_meal_plan = type_of_meal_plan  # Tipo de plano de refeição na reserva
        self.room_type_reserved = room_type_reserved  # Tipo de quarto reservado
        self.lead_time = lead_time  # Tempo antecipado de reserva
        self.market_segment_type = market_segment_type  # Tipo de segmento de mercado da reserva
        self.no_of_special_requests = no_of_special_requests  # Número de pedidos especiais na reserva
        self.booking_status = booking_status  # Status da reserva
        self.arrival_year = arrival_year  # Ano de chegada
        self.arrival_month = arrival_month  # Mês de chegada
        self.arrival_date = arrival_date  # Data de chegada


