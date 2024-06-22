
/**
 * Script para a funcionalidade de busca de personagens por nome na API de Rick and Morty.
 */

document.addEventListener('DOMContentLoaded', function () {
    const searchButton = document.getElementById('searchButton');
    const searchInput = document.getElementById('searchInput');
    const charactersList = document.getElementById('characters');

    searchButton.addEventListener('click', async () => {
        const name = searchInput.value.trim();
        charactersList.innerHTML = ''; 
        let errorMessage = "";

        try {
            const characters = await window.getRickAndMortyCharacters(name);
            if (characters.length === 0) {
                errorMessage = "Nenhum personagem encontrado.";
                window.setErrorMessage(errorMessage);
                return;
            }
            window.setErrorMessage(errorMessage); 

            characters.forEach(character => {
                const characterDiv = document.createElement("div");
                characterDiv.classList.add("character");

                const nameElement = document.createElement("h2");
                nameElement.textContent = character.name;

                const image = document.createElement("img");
                image.src = character.image;
                image.alt = `Imagen de ${character.name}`;
                image.classList.add("character-image");

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

                charactersList.appendChild(characterDiv);
            });
        } catch (error) {
            errorMessage = "Erro ao buscar os personagens.";
            window.setErrorMessage(errorMessage);
        }
    });
});
