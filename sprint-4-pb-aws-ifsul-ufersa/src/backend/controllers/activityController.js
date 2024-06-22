const axios = require("axios"); //  Biblioteca usada para fazer requisições HHTP
const Activity = require("../models/Activity");   //  Classe Activity
const { generateUUID, formatPercentage } = require("../service/activityService"); //  Service Activity

//  Método para acessar API do boredapi
const activityController = async (req, res) => {
  try {
    const response = await axios.get('https://www.boredapi.com/api/activity');  // Endereço de acesso
    const { activity, type, participants, accessibility } = response.data;  //  Atributos do json

    const newActivity = new Activity(
      generateUUID(), //  Método para gerar o UUID
      activity,
      type,
      participants,
      formatPercentage(accessibility)
    );

    return res.status(200).json(newActivity); // Requisição deu certo
  } catch (error) {
    console.error('Erro ao buscar atividade:', error.message);
    return res.status(500).json({ error: 'Erro ao buscar atividade' }); //  Requisição falhou
  }
};

module.exports = activityController;


