/**
 * Script para manipulação de eventos de cliques nos botões de personagem aleatório e personagens vivos.
 
 */

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('randomCharacterButton').addEventListener('click', async () => {
        const charactersList = document.getElementById('characters');
        charactersList.innerHTML = ''; 
        try {
            const character = await window.getRandomCharacter();
            displayCharacter(character, charactersList);
        } catch (error) {
            window.setErrorMessage("Error al obtener personaje aleatorio.");
        }
    });

    document.getElementById('aliveCharactersButton').addEventListener('click', async () => {
        const charactersList = document.getElementById('characters');
        charactersList.innerHTML = ''; 
        try {
            const characters = await window.getAliveCharacters(); 
            characters.forEach(character => {
                displayCharacter(character, charactersList);
            });
        } catch (error) {
            window.setErrorMessage("Error al obtener personajes vivos.");
        }
    });
});
/**
 * Adiciona personagem ou personagens ao DOM.
 * @param {Object} character - O objeto do personagem a ser exibido.
 * @param {HTMLElement} container - O contêiner onde os personagens serão exibidos.
 */
function displayCharacter(character, container) {
    const characterDiv = document.createElement("div");
    characterDiv.classList.add("character");

    const nameElement = document.createElement("h2");
    nameElement.textContent = character.name;

    const image = document.createElement("img");
    image.src = character.image;
    image.alt = `Imagen de ${character.name}`;

    const species = document.createElement("p");
    species.textContent = `Espécie: ${character.species}`;

    const origin = document.createElement("p");
    origin.textContent = `Origem: ${character.origin}`;

    const status = document.createElement("p");
    status.textContent = `Status: ${character.status}`;

    characterDiv.appendChild(nameElement);
    characterDiv.appendChild(image);
    characterDiv.appendChild(species);
    characterDiv.appendChild(origin);
    characterDiv.appendChild(status);

    container.appendChild(characterDiv);
}
