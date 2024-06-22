/**
 * Controlador para obter um personagem aleatório da API de Rick and Morty.
 * Este controlador faz uma chamada ao serviço `getRandomCharacter` para buscar um personagem aleatório
 *
 * @param {Object} request Objeto de requisição do Express, não utilizado diretamente neste controlador.
 * @param {Object} response Objeto de resposta do Express. Usado para enviar a resposta ao cliente.
 * @returns {Promise<void>} Uma promessa que resolve quando a resposta é enviada.
 */
const { getRandomCharacter } = require('../services/rickAndMortyService');

const randomCharacterController = async (request, response) => {
    try {
        const character = await getRandomCharacter();
        response.json(character);
    } catch (error) {
        response.status(500).send(error.message);
    }
};

module.exports = randomCharacterController;
