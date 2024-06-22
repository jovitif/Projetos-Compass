# Análise de Imagens com o Amazon Rekonigtion e geração de texto apartir do Amazon Bedrock

Este projeto consiste em criar uma aplicação serverless que apartir de uma imagem inserida dentro de um bucket retorna ou a emoção da face ou frases que combinem com a imagem

***

## Índice
- [Desenvolvimento](#desenvolvimento)
- [Dificuldades Conhecidas](#dificuldades-conhecidas)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Como Utilizar o Sistema](#como-utilizar-o-sistema)
- [Arquitetura AWS](#arquitetura-aws)
- [Estrutura de Diretórios e Arquivos](#estrutura-de-diretórios-e-arquivos)
- [Integrantes](#integrantes)

***

## Desenvolvimento

O projeto foi desenvolvido em Python, utilizando uma estrutura baseada em Serverless para criar uma aplicação que apartir do bucket e do nome da imagem baseado na rota seja gerada um JSON com a emoção que a face tem, ou rótulos para imagens de pets. Após a construção das funções de cada uma das rotas, foi feito deploy e implementação das mesmas via Serverless Framework na plataforma da AWS, utilizando os serviços de API Gateway, Rekonigtion, Bedrock e Funções Lambda para funcionamento da API.

***

## Dificuldades Conhecidas:

- Problemas com o Prompt para o bedrock: Foi enfrentado alguns problemas com relação a criação do prompt para as dicas da v2, para conseguir uma resposta satisfatória do bedrock foi necessário muito tempo.


***
## Tecnologias utilizadas

<div style="display: inline_block">
  <table border="1">
    <tr>
        <th>Tecnologia</th>
        <th>Versão</th>
    </tr>
    <tr>
        <td> <a href=""><img align="left" alt="AWS" height="20" width="20" src="https://cdn.iconscout.com/icon/free/png-256/free-aws-3215369-2673787.png?f=webp"></a> AWS</td>
        <td>Current</td>
    </tr>
    <tr>
        <td> <a href=""><img align="left" alt="Lambda" height="20" width="20" src="https://upload.wikimedia.org/wikipedia/commons/e/e9/Amazon_Lambda_architecture_logo.png"></a> AWS Lambda</td>
        <td>Current</td>
    </tr>
    <tr>
        <td> <a href=""><img align="left" alt="Polly" height="20" width="20" src="https://static-00.iconduck.com/assets.00/ai-amazonrekognition-icon-425x512-n6j1rkt9.png"></a> Amazon Rekognition</td>
        <td>Current</td>
    </tr>
    <tr>
        <td> <a href=""><img align="left" alt="DynamoDB" height="20" width="20" src="https://www.outsystems.com/Forge_CW/_image.aspx/Q8LvY--6WakOw9afDCuuGbQ9u-QKbiqiEaG1FDMiKVo=/aws-bedrock-runtime-2023-01-04%2000-00-00-2024-05-07%2016-13-21"></a> Amazon Bedrock</td>
        <td>Current</td>
    </tr>
    <tr>
        <td> <a href=""><img align="left" alt="Serverless" height="20" width="20" src="https://cdn.icon-icons.com/icons2/2699/PNG/512/serverless_logo_icon_168838.png"></a> Serverless</td>
        <td>v.3.38.0</td>
    </tr>
    <tr>
        <td> <a href=""><img align="left" alt="Python" height="20" width="20" src="https://w7.pngwing.com/pngs/234/329/png-transparent-python-logo-thumbnail.png"></a> Python</td>
        <td>v. 3.9</td>
    </tr>
    <tr>
        <td> <a href=""><img align="left" alt="Boto3" height="20" width="20" src="https://boto3typed.gallerycdn.vsassets.io/extensions/boto3typed/boto3-ide/0.5.4/1680224848596/Microsoft.VisualStudio.Services.Icons.Default"></a> Boto3</td>
        <td>v.1.34.74</td>
    </tr>
    </tr>
  </table>
</div>

***
## Como utilizar o Sistema

### Se o serviço estiver ativo:

Url's:

```
  GET - https://uc06urph01.execute-api.us-east-1.amazonaws.com/
  GET - https://uc06urph01.execute-api.us-east-1.amazonaws.com/v1
  GET - https://uc06urph01.execute-api.us-east-1.amazonaws.com/v2
  POST - https://uc06urph01.execute-api.us-east-1.amazonaws.com/v1/vision
  POST - https://uc06urph01.execute-api.us-east-1.amazonaws.com/v2/vision
```

- Abra o Postman
- Importe o arquivo do postman `sprint-8-pb-aws-ifsul-ufersa\tests\Sprint_08.postman_collection.json`
- Para as rotas POST no body da requisição adicione:
```
{
    "bucket": "bucket_de_exemplo",
    "imageName": "imagem.jpeg"
}
```

### Em caso de rodar localmente:

Clone este repositório
```
git clone -b grupo-2 https://github.com/Compass-pb-aws-2024-IFSUL-UFERSA/sprint-8-pb-aws-ifsul-ufersa.git
```
Baixe o Serverless Framework 
```
npm install -g serverless
npm i -D serverless-dotenv-plugin
```
Por fim adicione o bucket como variavel de ambiente e inicie a aplicação com o seguinte comando
```
serverless deploy
```

# Arquitetura AWS

<img width="500" src="assets/arquitetura-base.jpg">

***

## Estrutura de Diretórios e Arquivos
<div align= "left">
  <img width="200" src="./assets/estrutura_diretorios.png" alt="estrutura de arquivos">
</div>

## Integrantes
- [Leonardo Ennes](https://github.com/LeonardoEnnes)
- [João Vitor](https://github.com/jovitif)
- [Roger Lasch](https://github.com/rogerlasch)
- [Ygor Da Rosa](https://github.com/ygordarosa)
