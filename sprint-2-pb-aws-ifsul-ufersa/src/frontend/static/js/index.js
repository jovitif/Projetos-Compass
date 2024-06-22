const BASE_URL = window.location.origin;
const API_URL = `${BASE_URL}/api/v1`;
const WEATHER_ICONS = {
    "Encoberto com Chuvas Isoladas": "🌧",
    "Chuvas Isoladas": "🌧",
    "Chuva": "🌧",
    "Instável": "🌦",
    "Poss. de Pancadas de Chuva": "🌧",
    "Chuva pela Manhã": "🌧",
    "Chuva a Noite": "🌧",
    "Pancadas de Chuva a Tarde": "🌧",
    "Pancadas de Chuva pela Manhã": "🌧",
    "Nublado e Pancadas de Chuva": "🌧",
    "Pancadas de Chuva": "🌧",
    "Parcialmente Nublado": "🌥",
    "Chuvisco": "🌦",
    "Chuvoso": "🌧",
    "Tempestade": "⛈",
    "Predomínio de Sol": "🌞",
    "Encoberto": "🌥",
    "Nublado": "🌥",
    "Céu Claro": "🌞",
    "Nevoeiro": "🌥",
    "Geada": "🏔",
    "Neve": "🌨",
    "Não Definido": "🛸",
    "Pancadas de Chuva a Noite": "🌧",
    "Possibilidade de Chuva": "🌧",
    "Possibilidade de Chuva pela Manhã": "🌧",
    "Possibilidade de Chuva a Tarde": "🌧",
    "Possibilidade de Chuva a Noite": "🌧",
    "Nublado com Pancadas a Tarde": "🌧",
    "Nublado com Pancadas a Noite": "🌧",
    "Nublado com Poss. de Chuva a Noite": "🌧",
    "Nublado com Poss. de Chuva a Tarde": "🌧",
    "Nubl. c/ Poss. de Chuva pela Manhã": "🌧",
    "Nublado com Pancadas pela Manhã": "🌧",
    "Nublado com Possibilidade de Chuva": "🌧",
    "Variação de Nebulosidade": "🌥",
    "Chuva a Tarde": "🌧",
    "Poss. de Panc. de Chuva a Noite": "🌧",
    "Poss. de Panc. de Chuva a Tarde": "🌧",
    "Poss. de Panc. de Chuva pela Manhã": "🌧"
};

/**
 * Mostrar mensagem de erro para o usuário
 * @params {String} message
 */
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

/**
 * Retorna uma lista com todas as UF's
 * @returns {Array[String]} Lista com nome de todos os estados do país
 */
async function getStates() {
    let response = await fetch(`${API_URL}/states`);

    if (!response.ok) {
        throw new Error(await response.text());
    }

    let states = await response.json();
    
    return states;
}

/**
 * Busca a lista com nomes das cidades de um determinado estado.
 * @param {String} uf - Unidade federativa
 * @returns {Array[Object]} Lista das cidades
 */
async function getCitiesFromUF(uf) {
    let response = await (fetch(`${API_URL}/cities/${uf}`));

    if (!response.ok) {
        throw new Error(await response.text());
    }

    let cities = await response.json();
    
    return cities;
}

window.onload = async function () {
    const statesSelect = document.getElementById('statesSelect');
    const citiesSelect = document.getElementById('citiesSelect');
    let errorMessage = null;
    
    try {
        // Preencher o campo de estados
        let states = await getStates();
    
        states.forEach(state => {
            const option = document.createElement('option');
            option.value = state;
            option.textContent = state;
            statesSelect.appendChild(option);
        });
    } 
    catch (error) {
        errorMessage = 
            "😓 Desculpe, estamos passando por problemas tecnicos.\n"+
            "Tente novamente mais tarde.";
    }
    
    setErrorMessage(errorMessage);
    hideWeather();
};

/**
 * Atualiza as opções do campo de cidades
 */
async function updateCities() {
    const statesSelect = document.getElementById('statesSelect');
    const citiesSelect = document.getElementById('citiesSelect');
    const selectedState = statesSelect.value;

    citiesSelect.innerHTML = '';

    const defaultOption = document.createElement('option');
    defaultOption.value = '';
    defaultOption.textContent = 'Selecione um estado primeiro';
    citiesSelect.appendChild(defaultOption);
    
    if (selectedState) {
        let errorMessage = null;
        
        try {
            // Preencher o campo de cidades
            let cities = await getCitiesFromUF(selectedState);
            
            cities.forEach(city => {
                const option = document.createElement('option');
                option.value = city.name;
                option.textContent = city.name;
                citiesSelect.appendChild(option);
            });
        }
        catch (error) {
            errorMessage = 
                "😓 Desculpe, estamos passando por problemas tecnicos.\n"+
                "Tente novamente mais tarde.";
        }
        
        setErrorMessage(errorMessage);
    }
}

/**
 * Busca os dados referentes à previsão do tempo
 * @returns {Object} Dados da previsão do tempo
 */
async function getWeather() {
    const citiesSelect = document.getElementById('citiesSelect');
    const statesSelect = document.getElementById('statesSelect');
    
    let response = await fetch(`${API_URL}/weather/${citiesSelect.value}/${statesSelect.value}`);

    if (!response.ok) {
        throw new Error(await response.text());
    }

    let data = await response.json();

    return data;
}

/**
 * Mostra as informações de previsão do tempo para o usuário
 * @param {String} city 
 * @param {Number} temperature 
 * @param {String} status
 */
function showWeather(city, temperature, status) {
    const forecastCard = document.getElementById("forecastCard");
    const cityName = document.getElementById("cityName");
    const weatherIcon = document.getElementById("weatherIcon");
    const weatherTemperature = document.getElementById("temperature");
    const weatherStatus = document.getElementById("weatherStatus");

    // Modificar valores do card
    forecastCard.style.display = "";
    cityName.innerText = `📍 ${city}`;
    weatherIcon.innerText = WEATHER_ICONS[status];
    weatherTemperature.innerText = `${temperature} ºC`;
    weatherStatus.innerText =  status;
}

/**
 * Esconde o card da previsão do tempo
 */
function hideWeather() {
    const forecastCard = document.getElementById("forecastCard");
    forecastCard.style.display = "none";
}

/**
 * Verifica se os dados do formulário estão completos e válidos
 * @returns Estado da validação do formulário
 */
function validateFormData() {
    // Verificar os valores do formulário
    const statesSelect = document.getElementById('statesSelect');
    const citiesSelect = document.getElementById('citiesSelect');
    
    // Form inváida se cidade não estiver definida
    if (!citiesSelect.value) {
        return {
            valid: false,
            errorMessage: "Por favor informe qual cidade consultar."
        }
    }
    
    return { valid: true, errorMessage: null };
}

/**
 * Submete os valores do formulário e mostra o resultado
 * da requisição para o usuário
 * @param {SubmitEvent} event
 */
async function submitForm(event) {
    event.preventDefault();
    hideWeather();
    
    // Verificar os valores do formulário
    const { valid: isValid, errorMessage} = validateFormData();
    setErrorMessage(errorMessage);

    if (!isValid) {
        return;
    }
    
    // Consultar API e preencher interface
    try {
        let forecast = await getWeather();    
        let city = `${forecast.cidade}/${forecast.estado}`;
        let temperature = forecast.clima[0].max;
        let status = forecast.clima[0].condicao_desc;
        showWeather(city, temperature, status);
    } catch (error) {
        setErrorMessage('Desculpe, algo deu errado.');
    }
}