const { getCharacterByName } = require('../services/rickAndMortyService');

/**
 * Controlador para buscar personagens por nome na API Rick and Morty.
 * Utiliza o nome para buscar personagens correspondentes na API de Rick and Morty e retorna os resultados.
 * @param {Object} request - O objeto de requisição do Express, contendo os dados da query.
 * @param {Object} response - O objeto de resposta do Express.
 */
const searchCharacterController = async (request, response) => {
    try {
        const name = request.query.name;
        const characters = await getCharacterByName(name);
        response.json(characters);
    } catch (error) {
        console.error(error); 
        response.status(500).send({ message: "Error al procesar la solicitud", error: error.message });
    }
};

module.exports = searchCharacterController;
