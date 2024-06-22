const axios = require("axios");

/**
 * Faz o tratamento do nome das cidades
 * @param {String} city - Nome da cidade
 * @returns {String} Nome da cidade devidamente tratado
 */
const sanitizeCityName = (city) => {
    return city
        .replace(/\([^)]*\)/g, '') // Remover parentesis
        .replace('-', ' ') // Remover hífen
    ;
}

/**
 * Busca o ID de uma cidade atraves da API pública da BrasilAPI
 * @param {String} city - Nome da cidade
 * @param {String} state - Nome do estado
 * @returns ID da cidade informada ou null
 */
const getCityId = async (city, state) => {
    const { data } = await axios(`https://brasilapi.com.br/api/cptec/v1/cidade/${city}`);
    
    for (let cityData of data) {
        if (cityData.estado.toLowerCase() === state.toLowerCase()) {
            return cityData.id;
        }
    }
}

/**
 * Acessa a API pública da BrasilAPI e busca informações da previsão do tempo
 */
const weatherByCityController = async (request, response) => {
    try {
        // Busca informações da cidade
        const city = sanitizeCityName(request.params.city);
        const state = request.params.state;
        
        if (!city || !state) {
            return response.status(400).send("Requisição inválida.");
        }

        // Busca ID da cidade
        const cityId = await getCityId(city, state);
        if (cityId === null) {
            return response.status(400).send("Requisição inválida.");
        }

        // Busca previsão do tempo na cidade a partir do ID retornado anteriormente
        const { data: weatherData } = await axios(`https://brasilapi.com.br/api/cptec/v1/clima/previsao/${cityId}`);

        return response.json(weatherData);
    } catch (error) {
        return response.status(500).send(error.message);
    }
}

module.exports = weatherByCityController;
