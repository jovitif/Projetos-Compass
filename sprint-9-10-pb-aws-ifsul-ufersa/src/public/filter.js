document.addEventListener('DOMContentLoaded', function() {
    // Seleciona o elemento <select> dentro do elemento com a classe 'filter'
    const filterSelect = document.querySelector('.filter select');

    // Adiciona um evento de mudança ao elemento <select>
    filterSelect.addEventListener('change', function() {
        // Obtém o valor selecionado no menu suspenso
        const selectedFilter = filterSelect.value;
        
        // Seleciona todos os elementos com a classe 'animal-card'
        const animals = document.querySelectorAll('.animal-card');
        
        // Itera sobre todos os elementos 'animal-card'
        animals.forEach(animal => {
            // Verifica se o valor selecionado é vazio ou se a classe do animal corresponde ao valor selecionado
            if (selectedFilter === "" || animal.classList.contains(selectedFilter)) {
                // Se corresponder, exibe o animal
                animal.style.display = "block";
            } else {
                // Se não corresponder, oculta o animal
                animal.style.display = "none";
            }
        });
    });
});
