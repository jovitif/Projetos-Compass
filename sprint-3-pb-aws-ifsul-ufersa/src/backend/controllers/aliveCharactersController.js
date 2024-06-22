/**
 * Controlador para obter personagens vivos da API de Rick and Morty.

 *
 * @param {Object} request Objeto de requisição do Express.
 * @param {Object} response Objeto de resposta do Express. Usado para enviar a resposta.
 * @returns {Promise<void>} Uma promessa que resolve quando a resposta é enviada.
 */
const { getAliveCharacters } = require('../services/rickAndMortyService');

const aliveCharactersController = async (request, response) => {
    try {
        const aliveCharacters = await getAliveCharacters();
        response.json(aliveCharacters);
    } catch (error) {
        response.status(500).send(error.message);
    }
};

module.exports = aliveCharactersController;
