const express = require('express');
const router = express.Router();

router.get('/', async (req, res) => {
    res.status(200).send('Este é o app do Grupo 6 😀');
})

module.exports = router;
