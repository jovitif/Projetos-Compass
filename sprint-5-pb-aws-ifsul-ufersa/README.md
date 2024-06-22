# Hotel Reservations API com Machine Learning

Integrantes: João Sales, Kaio Fernando, Ricardo Ilan, Yefferson Silva

***

## 🔎 Índice
- [Desenvolvimento](#desenvolvimento)
- [Dificuldades](#dificuldades-conhecidas)
- [Tecnologias](#tecnologias)
- [Estrutura de Diretórios e Arquivos](#estrutura-de-diretórios-e-arquivos)
- [Teste](#teste-da-rota)
- [Como utilizar](#como-utilizar)

***

## 👷 Desenvolvimento
No início da sprint, focamos em assistir ao curso de Machine Learning na Udemy, por se tratar de um assunto novo. Após isso, nos reunimos para discutir o direcionamento do trabalho. Separamos as tarefas e começamos a experimentar modelos de ML com Jupyter Notebook. Tendo alguns modelos bem sucedidos, começamos a trabalhar na API. Criamos nossa API com Flask, e usamos a biblioteca Joblib para puxar o modelo do bucket S3. Quando conseguimos resultados satisfatórios nos testes, refatoramos o código e subimos o código para o Elastic Beanstalk da AWS, usando um container do docker.

***

## ⚔️ Dificuldades
- Carregar o modelo na API
- Construir a API em outra linguagem de programação (Python)
- Construir o modelo
- Deploy no Elastic Beanstalk

***

## 💻 Tecnologias

<div style="display: inline_block">

  <table border="1">
    <tr><th>Tecnologia</th>
      <td> <a href="https://developer.mozilla.org/en-US/docs/Web/python"><img align="center" alt="Js" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg"></a> Python</td>
      <td> <a href="https://jupyter.org/docs/latest/api/"><img align="center" alt="jupyter" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/jupyter/jupyter-original.svg"></a> Jupyter</td>
      <td> <a href="https://flaskjs.com/pt-br/"><img align="center" alt="flask" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg"></a> Flask</td>
      <td> <a href="https://pandas-http.com/docs/intro"><img align="center" alt="pandas" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg"></a> Pandas</td>
      <td> <a href="https://github.com/remy/scikitlearn#scikitlearn"><img align="center" alt="scikitlearn" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/scikitlearn/scikitlearn-original.svg"></a> Sklearn</td>
      <td> <a href="https://docs.aws.amazon.com/"><img align="center" alt="AWS" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg"></a> AWS CLI</td>
      <td> <a href="https://docs.aws.amazon.com/"><img align="center" alt="AWS" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original-wordmark.svg"></a> Docker</td>
</tr>
    <tr><th>Versão</th>
      <td>3.12.2</td>
      <td>7.0.8</td>
      <td>3.0.2</td>
      <td>2.2.1</td>
      <td>1.4.1</td>
      <td>2.15.22</td>
      <td>4.5.0</td>
    </tr>
  </table>
</div>

***

## 🗂️ Estrutura de Diretórios e Arquivos
```bash
└───src
    │   hotel_reservations.csv
    │
    ├───api
    │   │   main.py
    │   │   predictionController.py
    │   │   predictionService.py
    │   │   Reservation.py
    │   │
    │   └───__pycache__
    │
    └───ml
        │   testXgboost.ipynb
        │   xgboost.ipynb
        │
        └───sageMaker
                xgboostSagemaker.ipynb
```
***

## 🚌 Teste da rota

### POST /api/v1/predict

- `Request`
```json
{
    "no_of_adults": 2,
    "no_of_weekend_nights": 1,
    "no_of_week_nights": 2,
    "type_of_meal_plan": "Meal Plan 1",
    "room_type_reserved": "Room_Type 1",
    "lead_time": 207, 
    "arrival_year": 2018,
    "arrival_month": 12,
    "arrival_date": 30,
    "market_segment_type": "Offline",
    "no_of_special_requests": 0,
    "booking_status": "Not_Canceled"
}
```
- `Response`
```json
{
    "result": 3
}
```

***

## 🧑‍💻 Como utilizar

1. Pela URL

- `URL` [URL](http://sprint05-equipe02-docker-env.eba-erwcvtcc.us-east-1.elasticbeanstalk.com)

***

2. Pela linha de comando
- Clone este repositório para sua máquina com o comando `git clone`
- Instale as dependências solicitadas com `pip install`
- Em seu terminal, entre com o comando:
  ```bash
  cd sprint-5-pb-aws-ifsul-ufersa
  git checkout equipe-2
  cd src/api
  python main.py
  ```
-  Abra a URL pelo Postman e mande um POST request no modelo do teste acima

## 👥 Colaboradores

- Yefferson Silva - https://github.com/YeffersonSilva
- João Vitor - https://github.com/jovitif
- Kaio Fernando - https://github.com/kaio05
- Ricardo Ilan Dall'Agnol - https://github.com/Richoland

