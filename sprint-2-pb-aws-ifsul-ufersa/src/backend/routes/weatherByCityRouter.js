const express = require("express");
const router = express.Router();
const weatherByCityController = require("../controllers/weatherByCityController");

router.get("/:city/:state", weatherByCityController);

module.exports = router;

