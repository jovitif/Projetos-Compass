# Imagem base oficial do Node.js
FROM node:14

# Diretório de trabalho dentro do container
WORKDIR /usr/src/app

# package.json e o package-lock.json
COPY package*.json ./

# Instalação as dependências do projeto
RUN npm install

# Cópia do restante do código da aplicação
COPY . .

# Porta exposta que a aplicação irá rodar
EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["node", "./server/server.js"]
