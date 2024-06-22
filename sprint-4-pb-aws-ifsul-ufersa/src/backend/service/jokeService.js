const { v4: uuid } = require('uuid');

//  Método para gerar UUID
const generateUUID = () => {
    return uuid();
};

//  Método para formatar a data
const formatDate = (date) => {
    const formattedDate = new Date(date).toLocaleDateString('pt-BR').replaceAll('/', '-'); // Data no formato DD-MM-AAAA
    return formattedDate;
};

// Método para deixar "chuck norris" em maiúsculo
const formatJoke = (joke) => {
    const formattedJoke = joke.replaceAll("Chuck Norris", "CHUCK NORRIS"); // Transforma todas as instâncias de "Chuck Norris" em "CHUCK NORRIS"
    return formattedJoke
}

module.exports = { generateUUID, formatDate, formatJoke };


