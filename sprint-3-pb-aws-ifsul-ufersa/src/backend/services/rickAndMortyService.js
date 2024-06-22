

const axios = require('axios');
require('dotenv').config();

/**
 * Configura a instância do Axios com a URL base da API, obtida das variáveis de ambiente.
 */
const api = axios.create({
    baseURL: process.env.RICK_AND_MORTY_API_URL,
});

/**
 * Obtém todos os personagens da API Rick and Morty.
 *
 * @async
 * @function getAllCharacters
 * @returns {Promise<Object[]>} Uma promessa que resolve com a lista de todos os personagens mapeados para objetos simplificados.
 */
async function getAllCharacters() {
    const response = await api.get();
    return response.data.results.map(mapCharacterData);
}

/**
 * Obtém personagens vivos da API Rick and Morty.
 *
 * @async
 * @function getAliveCharacters
 * @returns {Promise<Object[]>} Uma promessa que resolve com a lista de personagens vivos, cada um mapeado para um objeto simplificado.
 */
async function getAliveCharacters() {
    const response = await api.get('/?status=alive');
    return response.data.results.map(mapCharacterData);
}

/**
 * Obtém um personagem aleatório da API Rick and Morty.
 *
 * @async
 * @function getRandomCharacter
 * @returns {Promise<Object>} Uma promessa que resolve com os dados de um personagem aleatório, mapeado para um objeto simplificado.
 */
async function getRandomCharacter() {
    const randomId = Math.floor(Math.random() * 671) + 1;
    const response = await api.get(`/${randomId}`);
    return mapCharacterData(response.data);
}



async function getCharacterByName(name) {
    const response = await api.get(`/?name=${encodeURIComponent(name)}`);
    return response.data.results.map(mapCharacterData);
}


/**
 * Mapeia os dados brutos de um personagem para um objeto simplificado.
 *
 * @param {Object} character O objeto do personagem obtido da API.
 * @returns {Object} Um objeto simplificado contendo apenas nome, espécie, imagem, status e origem do personagem.
 */
function mapCharacterData(character) {
    return {
        name: character.name,
        species: character.species,
        image: character.image,
        status: character.status,
        origin: character.origin.name,
    };
}

module.exports = {
    getAllCharacters,
    getCharacterByName,
    getAliveCharacters,
    getRandomCharacter,
};
