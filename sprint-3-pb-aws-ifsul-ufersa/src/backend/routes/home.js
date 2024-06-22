const express = require("express");
const router = express.Router();
const path = require("path")

router.get("/", (req, resp) => {
    resp.sendFile(path.join(__dirname, "../../frontend/index.html"));
})

module.exports = router;
