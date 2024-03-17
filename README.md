# Previsão de Vendas com Azure Machine Learning e Flask

Este projeto consiste na construção de um modelo de previsão de vendas utilizando o Azure Machine Learning para treinar o modelo e Flask para criar uma API que disponibiliza as previsões.
Azure Machine Learning

O Azure Machine Learning foi utilizado para treinar o modelo de previsão de vendas. Os passos realizados foram:

## Preparação dos Dados:
Os dados de vendas e características dos produtos foram carregados no Azure Machine Learning.
Foram realizadas as etapas de pré-processamento, como tratamento de valores ausentes, codificação de variáveis categóricas e normalização dos dados, se necessário.

## Treinamento do Modelo:
Um modelo de regressão, como Random Forest ou Regressão Linear, foi escolhido e treinado utilizando os dados preparados.
O desempenho do modelo foi avaliado usando métricas como RMSE e R².

## Registro do Modelo:
O modelo treinado foi registrado no Azure Machine Learning para facilitar o acesso e implantação posteriormente.

## Flask API

Uma API foi desenvolvida usando Flask para disponibilizar o modelo treinado. Os passos realizados foram:

### Implementação da API:
Utilizando Flask, foi criada uma API com um ponto de extremidade para receber os dados necessários para a previsão de vendas.

### Integração com o Modelo:
O modelo treinado, registrado no Azure Machine Learning, foi integrado à API para realizar as previsões de vendas com base nos dados recebidos.

## Como Usar a API

Para utilizar a API de previsão de vendas, você pode enviar uma solicitação POST para o ponto de extremidade fornecido. Certifique-se de enviar os dados no formato correto conforme especificado na documentação da API.

Exemplo de solicitação usando Python e a biblioteca requests:

python

import requests

url = "http://endereco-da-api.com/prever_vendas"
dados = {
    "preco": 20.50,
    "promocao": True,
    "quantidade": 100,
    "tipo_produto": "eletronico"
}

resposta = requests.post(url, json=dados)
print(resposta.json())

## Estrutura do Repositório

    README.md: Este arquivo contendo a descrição do projeto e os passos realizados.
    azure_ml_training.ipynb: O notebook Jupyter contendo o código utilizado para preparação dos dados e treinamento do modelo no Azure Machine Learning.
    flask_api.py: O código-fonte da API Flask para disponibilizar o modelo de previsão.
    requirements.txt: Um arquivo contendo as dependências necessárias para executar a API Flask.

## Como Executar

Para executar a API Flask localmente, siga as etapas abaixo:

    Clone este repositório em sua máquina local.
    Instale as dependências necessárias executando pip install -r requirements.txt.
    Execute o arquivo flask_api.py com o comando python flask_api.py.
    A API estará disponível no endereço http://localhost:5000.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
## Licença

Este projeto está licenciado sob a MIT License.

