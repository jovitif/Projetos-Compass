const express = require('express');
const router = express.Router();
const axios = require('axios');
const path = require('path');
const dotenv = require('dotenv');
const {findByTelefone} = require('../public/animalService')

// Carregar variáveis de ambiente do arquivo .env
dotenv.config({ path: path.resolve(__dirname, '.env') });

// Rota home
router.get('/', (req, res) => {
    // res.send('Olá! Bem-vindo ao Reencontro de Animais.');
    res.redirect('/encontrados');
});

// Rota encontrados
router.get('/encontrados', async (req, res) => {
    // res.send(`Aqui tem os animais encontrados.`);
    const found = await axios.get(process.env.BASE_API_URL + '/encontrados');
    const found_animals = found.data;

    foundActive = true;

    return res.render('found', { found_animals, foundActive })
});

// Rota perdidos
router.get('/perdidos', async (req, res) => {
    // res.send(`Aqui tem os animais perdidos.`);
    const lost = await axios.get(process.env.BASE_API_URL + '/perdidos');
    const lost_animals = lost.data;

    foundActive = false;
    
    return res.render('lost', { lost_animals, foundActive})
});

// Rota para a página de detalhes do animal
router.get('/animal/:telefone', async (req, res) => {
    const telefone = req.params.telefone;
    const categoria = req.query.categoria;
    const imageurl = req.query.imageurl;

    const animal = await findByTelefone(telefone, categoria, imageurl);

    // Se os detalhes do animal forem encontrados, renderize a página de detalhes
     res.render('animal_details', {animal, isDetailPage: true});
});

module.exports = router;