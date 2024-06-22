const axios = require('axios');

// Função para buscar os detalhes do animal com base no telefone
async function findByTelefone(telefone, categoria, imageurl) {
    let pagina = '';
    try {
        // Faça a requisição para obter os detalhes do animal com base no telefone
        if(categoria === 'perdido') {
            pagina = 'perdidos';
        } else {
            pagina = 'encontrados';
        }
        const response = await axios.get(`${process.env.BASE_API_URL}/${pagina}?telefone=${telefone}`);
        const animais = response.data; 
        
        // Filtrar o animal com base na imageurl
        const animalClicado = animais.find(animal => animal.imageurl === imageurl);

        return animalClicado;
    } catch (error) {
        console.error('Erro ao buscar animal por telefone:', error);
        throw error;
    }
}

module.exports = {findByTelefone};