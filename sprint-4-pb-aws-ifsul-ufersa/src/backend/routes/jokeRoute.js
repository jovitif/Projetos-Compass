const express = require("express");
const jokeController = require("../controllers/jokeController");

const router = express.Router();

// Rota principal
router.get("/", jokeController)

module.exports = router 