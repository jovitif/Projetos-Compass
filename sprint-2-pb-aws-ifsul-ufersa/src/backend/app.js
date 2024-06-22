const express = require("express")
const allStatesRouter = require("./routes/allStatesRouter")
const allCitiesRouter = require("./routes/allCitiesRouter")
const weatherByCityRouter = require("./routes/weatherByCityRouter")
const homeRouter = require("./routes/home")
const path = require("path")
const dotenv = require('dotenv');

dotenv.config();

const PORT = process.env.PORT

const app = express()

app.use("/api/v1/states", allStatesRouter)
app.use("/api/v1/cities", allCitiesRouter)
app.use("/api/v1/weather", weatherByCityRouter)
app.use("/", homeRouter)
app.use("/static", express.static(path.join(__dirname, "../frontend/static")))

app.listen(PORT, () => console.log("Server is running!"))
