const express = require("express"); //  Biblioteca para trabalhar com rotas
const activityController = require("../controllers/activityController");    //  Controller de Atividades
const router = express.Router();    //  Usando rotas
router.get("/", activityController);    // Fazendo o get de Atividades

module.exports = router;
