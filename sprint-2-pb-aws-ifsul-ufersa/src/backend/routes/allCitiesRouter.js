const express = require("express");
const router = express.Router();
const allCitiesByStateController = require("../controllers/allCitiesByStateController");

router.get("/:state", allCitiesByStateController);

module.exports = router;
