// Importando as dependências
const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

// Configurando o Express
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware para analisar o corpo das solicitações como JSON
app.use(bodyParser.json());

// Rota para a página inicial
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

// Rota para lidar com a solicitação de conversão de texto para áudio
app.post('/converter', async (req, res) => {
    try {
        const frase = req.body.frase;
        const versaoApi = req.body.versaoApi;

        // Formato da frase para o corpo da solicitação
        const data = {
            phrase: frase
        };

        // Fazendo a solicitação para a API de conversão de texto para áudio usando Axios
        const response = await axios.post(`https://9p01p3ntjg.execute-api.us-east-1.amazonaws.com/${versaoApi}/tts`, data);

        // Verificando se a solicitação foi bem-sucedida
        if (response.status !== 200) {
            throw new Error('Erro ao converter texto em áudio');
        }

        // Convertendo a resposta para JSON
        const responseData = response.data;

        // Enviando a URL do áudio como resposta
        res.json({ url_to_audio: responseData.url_to_audio });
    } catch (error) {
        // Lidando com erros
        console.error(error);
        res.status(500).json({ error: 'Ocorreu um erro ao converter o texto em áudio' });
    }
});

// Iniciando o servidor
app.listen(PORT, () => {
    console.log(`Servidor rodando em http://localhost:${PORT}`);
});
