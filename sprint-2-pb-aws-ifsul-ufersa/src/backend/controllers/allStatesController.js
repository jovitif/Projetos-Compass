const axios = require("axios")

/**
 * Busca lista com nome de todos os estados brasileiros
 * através da API pública
 * @param {Request} request 
 * @param {Response} response 
 * @returns Retorna a resposta enviada para o cliente
 */
const allStatesController = async (request, response) => {
    try {
        const { data } = await axios(`https://brasilapi.com.br/api/ibge/uf/v1/`) 

        const allUfs = data.map((state) => {
            return state.sigla
        }) 

        return response.json(allUfs)
    } catch (error) {
        return response.status(500).send(error.message)
    }
}

module.exports = allStatesController