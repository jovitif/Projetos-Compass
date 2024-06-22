const express = require('express');
const app = express();
const routes = require('./routes');  
const exphbs = require("express-handlebars");
const path = require("path");
const dotenv = require('dotenv');

// Carregar variáveis de ambiente do arquivo .env
dotenv.config({ path: path.resolve(__dirname, '.env') });


// Configuração do Handlebars com o helper 'containsDog'
const hbs = exphbs.create({
  defaultLayout: 'main',
  extname: '.handlebars',
  helpers: {
      containsDog: function(array) {
          return array.includes('Dog') ? 'cachorro' : 'gato';
      }
  }
});

// configura o middleware para servir arquivos estáticos
app.use(express.static(path.join(__dirname, "../public")));

// configura o mecanismo de visualização
app.set("views", path.join(__dirname, "../views"));
app.engine('handlebars', hbs.engine);
app.set("view engine", "handlebars");

// Middleware para definir a variável phoneNumber em todas as rotas
app.use((req, res, next) => {
  res.locals.phoneNumber = process.env.PHONE_NUMBER;
  next();
});

app.use(routes);

// Inicia o servidor
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor rodando na porta ${PORT}`);
});

// app.use((req, res) => {
//   res.status(404).send('Página não encontrada');
// });