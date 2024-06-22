import express from 'express';
import { getAnimaisPerdidos, getAnimaisEncontrados } from './animalController';

const app = express();
app.use(express.json());

app.get('/animais/perdidos', getAnimaisPerdidos);
app.get('/animais/encontrados', getAnimaisEncontrados);

export default app;
