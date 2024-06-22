const express = require("express");
const router = express.Router();
const allStatesController = require("../controllers/allStatesController");

router.get("/", allStatesController);

module.exports = router;




