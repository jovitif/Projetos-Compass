const axios = require("axios");
const Joke = require("../models/Joke");
const { generateUUID, formatDate, formatJoke } = require("../service/jokeService")

const jokeController = async (req, res) => {
    try {
        const response = await axios.get("https://api.chucknorris.io/jokes/random");
        const { created_at, updated_at, icon_url, url, value } = response.data;

        const joke = new Joke(
            formatDate(updated_at), // Data formatada como DD-MM-AAAA
            formatDate(created_at), // Data formatada como DD-MM-AAAA
            icon_url,
            generateUUID(), // GUID gerado randômicamente
            formatJoke(value), // Piada com "Chuck Norris" em caixa alta
            url,
        )

        return res.status(200).json(joke)
    } catch (err) {
        // Requisição falhou
        console.error("Erro ao buscar piada: ", err);
        return res.status(500).json({ error: "Erro ao buscar piada" })
    }
}

module.exports = jokeController