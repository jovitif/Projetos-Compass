//  Classe service contendo os métodos de geração de UUID e formatação de porcentagem
const { v4: uuid } = require('uuid'); //  Importando biblioteca de geração de UUID

//  Método para gerar UUID
const generateUUID = () => {
  return uuid(); // Padrão de formato {XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}
};

//  Método para formatar em porcentagem
const formatPercentage = (num) => {
  const formatado = `${Math.round(num * 100)}%`;  //  Multiplica por 100 e arredonda para inteiro
  return formatado;
};

module.exports = { generateUUID, formatPercentage };  //  Exportar os métodos criados

