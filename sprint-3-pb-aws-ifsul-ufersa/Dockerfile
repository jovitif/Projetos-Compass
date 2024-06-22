# Plataforma
FROM node:latest

# Define o ambiente Node como produção por padrão.
ENV NODE_ENV production

# Define o diretório de trabalho para /usr/src/app.
WORKDIR /usr/src/app

# Baixa as dependências como uma etapa separada para aproveitar o cache do Docker.
# Aproveita um ponto de montagem de cache em /root/.npm para acelerar builds subsequentes.
# Aproveita pontos de montagem de bind para package.json e package-lock.json para evitar a necessidade de copiá-los
# para esta camada.
RUN --mount=type=bind,source=package.json,target=package.json \
    --mount=type=bind,source=package-lock.json,target=package-lock.json \
    --mount=type=cache,target=/root/.npm \
    npm ci --omit=dev

# Executa a aplicação como um usuário não-root.
USER node

# Copia o restante dos arquivos de origem para a imagem.
COPY . . 

# Expõe a porta em que a aplicação escuta.
EXPOSE 3000

# Executa a aplicação.
CMD node src/backend/app.js