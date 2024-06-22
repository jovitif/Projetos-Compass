const express = require("express");
const router = express.Router();
const allCharactersController = require("../controllers/allCharactersController");
const randomCharacterController = require("../controllers/randomCharacterController");
const aliveCharactersController = require('../controllers/aliveCharactersController');
const searchCharacterController = require('../controllers/searchCharacterController');

router.get("/", allCharactersController);


/**
 * Rota para obter um personagem aleatório.
 * @name get/random
 * @function
 * @param {string} '/random' - Endpoint para um personagem aleatório.
 * @param {function} randomCharacterController - Controlador para a solicitação.
 */
router.get("/random", randomCharacterController);

router.get('/alive', aliveCharactersController);

router.get("/search", searchCharacterController);

module.exports = router;
