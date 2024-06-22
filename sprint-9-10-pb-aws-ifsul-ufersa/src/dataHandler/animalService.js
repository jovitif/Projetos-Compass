import AWS from 'aws-sdk';

const dynamoDb = new AWS.DynamoDB.DocumentClient();
const TBL_NAME = process.env.TBL_NAME;

const scanDynamoDB = async (params) => {
  try {
    const data = await dynamoDb.scan(params).promise();
    return data.Items;
  } catch (error) {
    console.log(error);
    throw new Error('Erro ao acessar o DynamoDB');
  }
};

export const getAnimaisPorCategoria = async (categoria, caracteristica) => {
  const params = {
    TableName: TBL_NAME,
    FilterExpression: "#categoria = :categoria" + (caracteristica ? " AND contains(#caracteristicas, :caracteristica)" : ""),
    ExpressionAttributeNames: {
      "#categoria": "categoria",
      ...(caracteristica && { "#caracteristicas": "caracteristicas" }),
    },
    ExpressionAttributeValues: {
      ":categoria": categoria,
      ...(caracteristica && { ":caracteristica": caracteristica }),
    },
  };

  return scanDynamoDB(params);
};
