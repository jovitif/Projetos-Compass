const BASE_URL = window.location.origin; //Obter URL da para se conectar a API
const API_URL = `${BASE_URL}/api/v1/characters`;


//Função para obter personagens
async function getRickAndMortyCharacters(name = "") {
    let url = API_URL;
    if (name) {
        url += `/search?name=${encodeURIComponent(name)}`;
    }

    let response = await fetch(url);
    if (!response.ok) {
        throw new Error(await response.text());
    }
    let characters = await response.json();
    return characters;
}

window.getRickAndMortyCharacters = getRickAndMortyCharacters;
window.setErrorMessage = setErrorMessage;

//  * Busca un personaje aleatório na API de Rick and Morty.


async function getRandomCharacter() {
    try {
        const response = await fetch('/api/v1/characters/random');
        if (!response.ok) {
            throw new Error('Respuesta de red no fue ok.');
        }
        const character = await response.json();
        return character;
    } catch (error) {
        console.error("Error al obtener un personaje aleatorio:", error);
        throw error;
    }
}
// * Busca todos os personagens vivos na API de Rick and Morty.
async function getAliveCharacters() {
    try {
        const response = await fetch('/api/v1/characters/alive');
        if (!response.ok) {
            throw new Error('Respuesta de red no fue ok.');
        }
        const characters = await response.json();
        return characters;
    } catch (error) {
        console.error("Error al obtener personajes vivos:", error);
        throw error;
    }
}


window.getRandomCharacter = getRandomCharacter;
window.getAliveCharacters = getAliveCharacters;

// Carrega no html todos os personagens da serie na div
window.onload = async function () {
    const charactersList = document.getElementById('characters');
    let errorMessage = null;

    try {
        let characters = await getRickAndMortyCharacters();

        characters.forEach(character => {
            const characterDiv = document.createElement("div");
            characterDiv.classList.add("character");

            const name = document.createElement("h2");
            name.textContent = character.name;

            const status = document.createElement("p");
            status.textContent = "Status: " + character.status;

            const image = document.createElement("img");
            image.src = character.image;
            image.alt = character.name;

            const species = document.createElement("p");
            species.textContent = "Espécie: " + character.species;

            const origin = document.createElement("p");
            origin.textContent = "Origem: " + character.origin;

            characterDiv.appendChild(name);
            characterDiv.appendChild(image);
            characterDiv.appendChild(species);
            characterDiv.appendChild(origin);
            characterDiv.appendChild(status);

            charactersList.appendChild(characterDiv);
        });
    } catch (error) {
        errorMessage =
            "Erro ao carregar os personagens.\n"
    }

    setErrorMessage(errorMessage);
};

//Caso tenha algum erro na API ela retorna uma mensagem de erro
function setErrorMessage(message) {
    const errorMessage = document.getElementById("errorMessage");

    if (message) {
        errorMessage.innerText = message;
        errorMessage.hidden = false;
    } else {
        errorMessage.innerText = "";
        errorMessage.hidden = true;
    }
}

window.getRickAndMortyCharacters = getRickAndMortyCharacters;
window.setErrorMessage = setErrorMessage;
