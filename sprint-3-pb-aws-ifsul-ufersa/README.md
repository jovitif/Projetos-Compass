<h1 align="center">Projeto Rick and Morty API</h1>

<p align="justify">
  A API Rick and Morty é uma API REST(ish) e GraphQL baseada no programa de televisão Rick and Morty. Você terá acesso a cerca de centenas de personagens, conforme visto no programa de TV.
</p>

***

## 🌐 Índice

- [Desenvolvimento](#descrição-do-projeto)
  - [Dificuldades Desconhecidas](#dificuldades-desconhecidas)
  - [Como Utilizar o Sistema](#como-utilizar-o-sistema)
- [Estrutura das Pastas](#estrutura-das-pastas)
- [Tecnologias utilizadas](#tecnologias-utilizadas)
- [Funcionamento](#funcionamento)

## 📑 Desenvolvimento
Este projeto foi desenvolvido utilizando **Node.js** como ambiente de execução para o JavaScript, e **Express** como framework web para criar o backend e consumir os dados da API selecionada. No frontend, concentramo-nos em criar uma interface de usuário intuitiva e interativa, utilizando HTML e CSS para estilização.
Foi utilizado o **Docker** para garantir uma consistência no ambiente de execução, e hospedamos a aplicação dockerizada em uma instância dentro da **AWS Cloud**, tornando a API acessível online.

###  🤔  Dificuldades Desconhecidas
Durante o desenvolvimento, enfrentamos desafios com duas ferramentas novas para nossa equipe:

- **Docker**: Encontramos dificuldades devido à falta de familiaridade com a ferramenta. No entanto, superamos esses obstáculos por meio de pesquisa e experimentação.

- **AWS**: Por ser uma plataforma que nunca utilizamos anteriormente, tivemos dificuldades com a criação de instâncias e implantação do projeto para disponibilização online. Apesar disso, conseguimos superar os obstáculos com persistência e aprendizado contínuo.


### ⚙️  Como Utilizar o Sistema

Para utilizar o sistema, siga estas etapas:

1. Clone este repositório executando o seguinte comando no terminal:
`git clone -b equipe-4 --single-branch https://github.com/Compass-pb-aws-2024-IFSUL-UFERSA/sprint-3-pb-aws-ifsul-ufersa.git`

2. Após o clone, navegue até o diretório do projeto: `cd sprint-3-pb-aws-ifsul-ufersa`

3. Instale todas as dependências necessárias com: `npm install`.

4. Caso encontre um arquivo chamado .env.example. Faça uma cópia deste arquivo e renomeie-o para .env. Em seguida, abra o arquivo .env e insira as seguintes configurações: `PORT=3000
RICK_AND_MORTY_API_CHARACTERS=https://rickandmortyapi.com/api/character/`

5. Para iniciar o servidor de desenvolvimento, execute o comando: ´npm run dev´

6. Abra seu navegador e acesse a porta 3000 para visualizar a aplicação em execução.

## 📂 Estrutura das Pastas

```
sprint-3-pb-aws-ifsul-ufersa/
├── node_modules/
├── src 
│   ├── backend
│   │   ├── controllers
│   │   │   ├── aliveCharactersController.js
│   │   │   ├── allCharactersController.js
│   │   │   ├── randomCharacterController.js
│   │   │   └── searchCharacterController.js
│   │   ├── routes
│   │   │   ├── allCharactersRouter.js
│   │   │   └── home.js
│   │   ├── services
│   │   │   └── rickAndMortyService.js
│   │   └── app.js
│   └── frontend
│       ├── static
│       │   ├── css
│       │   │   └── style.css
│       │   └── js
│       │       ├── index.js
│       │       ├── random.js
│       │       └── search.js
│       └── index.html
├── .dockerignore
├── .env
├── .gitignore
├── compose.yaml
├── Dockerfile
├── package-lock.json
├── package.json
└── README.md
```

## 🛠️ Tecnologias utilizadas
- ![JavaScript](https://img.shields.io/badge/-JavaScript-yellow)
- ![HTML & CSS](https://img.shields.io/badge/-HTML%20%26%20CSS-orange)
- ![Node.js](https://img.shields.io/badge/-Node.js-green)
- ![Express](https://img.shields.io/badge/-Express-blue)
- ![Nodemon](https://img.shields.io/badge/-Nodemon-lightgrey)
- ![Docker](https://img.shields.io/badge/-Docker-blueviolet)
- ![AWS CLI](https://img.shields.io/badge/-AWS%20CLI-orange)
- 
## ▶️ Funcionamento
[teste-aplicacao.webm](https://github.com/Compass-pb-aws-2024-IFSUL-UFERSA/sprint-3-pb-aws-ifsul-ufersa/assets/86473140/4e213315-929e-4969-9c2f-7aeaa9ad2d14)

