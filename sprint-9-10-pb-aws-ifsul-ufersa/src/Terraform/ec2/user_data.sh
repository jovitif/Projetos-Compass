#!/bin/bash

# Atualizar o sistema
sudo yum update -y

# Instalar Docker e Git
sudo amazon-linux-extras install docker -y
sudo yum install -y git

# Iniciar o serviço Docker
sudo service docker start

# Adicionar o usuário ec2 ao grupo docker
sudo usermod -a -G docker ec2-user

# Variáveis de ambiente
github_association="${github_association}"
github_repo="${github_repo}"
github_token="${github_token}"

# Clonar o repositório Git
sudo -u ec2-user git clone https://${github_token}@github.com/${github_association}/${github_repo}.git /home/ec2-user/${github_repo}

# Ajustar permissões no diretório clonado
sudo chown -R ec2-user:ec2-user /home/ec2-user/${github_repo}

# Adicionar exceção para safe.directory no Git após a clonagem
sudo -u ec2-user git config --global --add safe.directory /home/ec2-user/${github_repo}

# Navegar para o diretório clonado e trocar de branch
sudo -u ec2-user git -C /home/ec2-user/${github_repo} switch "grupo-2"

# Renomear o arquivo .env.example para .env
sudo -u ec2-user mv /home/ec2-user/${github_repo}/src/server/.env.example /home/ec2-user/${github_repo}/src/server/.env

# Construir e rodar o Docker
cd /home/ec2-user/${github_repo}/src
sudo docker build -t website-image .
sudo docker run -d -p 3000:3000 website-image