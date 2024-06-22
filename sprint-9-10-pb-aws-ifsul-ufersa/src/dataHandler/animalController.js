import { getAnimaisPorCategoria } from './animalService';

export const getAnimaisPerdidos = async (req, res) => {
  const { caracteristica } = req.query;
  try {
    const animais = await getAnimaisPorCategoria('perdido', caracteristica);
    return res.json(animais);
  } catch (error) {
    res.status(500).json({ error: 'Não foi possível retornar a lista de animais perdidos' });
  }
};

export const getAnimaisEncontrados = async (req, res) => {
  const { caracteristica } = req.query;
  try {
    const animais = await getAnimaisPorCategoria('encontrado', caracteristica);
    return res.json(animais);
  } catch (error) {
    res.status(500).json({ error: 'Não foi possível retornar a lista de animais encontrados' });
  }
};
