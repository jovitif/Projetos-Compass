const express = require("express");
const allStatesRouter = require('./routes/allCharactersRouter')
const homeRouter = require('./routes/home')
const path = require("path")



require('dotenv').config();
const PORT = process.env.PORT

console.log(`PORT: ${PORT}`)

const app = express();

app.use("/api/v1/characters", allStatesRouter)

app.use("/", homeRouter)
app.use("/static", express.static(path.join(__dirname, "../frontend/static")))


app.listen(PORT, (error) => {
  if (error) {
    console.error("Error:", error);
  } else {
    console.log(`Server is running! PORT= ${PORT}`);
  }
});