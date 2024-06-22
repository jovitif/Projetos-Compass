const express = require("express");
// Configura variáveis de ambiente
require("dotenv").config();

const mainRoute = require('./routes/mainRoute');
const jokeRoute = require('./routes/jokeRoute');
const activityRoute = require('./routes/activityRouter');

const app = express();
const PORT = process.env['PORT'];

// Configurnado o Swagger
const swaggerUi = require('swagger-ui-express');
const swaggerFile = require('./swagger_output.json');
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerFile));

// Rota /
app.use('/', mainRoute);
// Rota /api/piadas
app.use('/api/piadas', jokeRoute);
// Rota /api/atividades
app.use('/api/atividades', activityRoute);

app.listen(PORT, () => {
    console.log("Rodando na porta", PORT);
})
