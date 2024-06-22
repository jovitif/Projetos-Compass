const axios = require("axios");

/**
 * Busca lista com nome de todas as cidades de um determinado
 * estado brasileiro através da API pública
 * @param {Request} request 
 * @param {Response} response 
 * @returns Retorna a resposta enviada para o cliente
 */
const allCitiesByStateController = async (request, response) => {
    try {
        const { state } = request.params;

        const providers = "dados-abertos-br,gov,wikipedia";
        const url = `https://brasilapi.com.br/api/ibge/municipios/v1/${state}?providers=${providers}`;

        const { data } = await axios(url);

        const cities = data.map((city) => {
            return {
                name: city.nome,
                code: city.codigo_ibge
            };
        });

        return response.json(cities);
    } catch (error) {
        return response.status(500).send(error.message);
    }
}

module.exports = allCitiesByStateController;
