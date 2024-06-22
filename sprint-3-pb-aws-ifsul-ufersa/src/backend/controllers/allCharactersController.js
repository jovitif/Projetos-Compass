/**
 * Controlador para todos os personagens da API de Rick and Morty.
 * Este controlador faz uma chamada ao serviço `getAllCharacters` para buscar todos os personagens
 *
 * @param {Object} request Objeto de requisição do Express, não utilizado diretamente neste controlador.
 * @param {Object} response Objeto de resposta do Express. Usado para enviar a resposta ao cliente.
 * @returns {Promise<void>} Uma promessa que resolve quando a resposta é enviada.
 */
const { getAllCharacters } = require('../services/rickAndMortyService');

const allCharactersController = async (request, response) => {
    try {
        const allCharacters = await getAllCharacters();

        return response.json(allCharacters);
    } catch (error) {

        return response.status(500).send(error.message);

    }
};

module.exports = allCharactersController;
