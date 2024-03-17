# Previsão de Vendas

Este projeto consiste na construção de um modelo de previsão de vendas utilizando técnicas de aprendizado de máquina. O objetivo é prever as vendas de um determinado produto com base em diversas variáveis, como preço, promoções, e outras características.
Passos do Projeto
## 1. Preparação dos Dados

    Coleta dos dados de vendas e das características dos produtos.
    Pré-processamento dos dados para lidar com valores ausentes, outliers e codificação de variáveis categóricas.
    Divisão dos dados em conjuntos de treinamento e teste.

## 2. Escolha do Modelo

    Teste de vários algoritmos de regressão, como regressão linear, árvores de decisão e modelos de ensemble.
    Avaliação do desempenho de cada modelo utilizando métricas como RMSE (Root Mean Squared Error) e R² (coeficiente de determinação).

## 3. Treinamento do Modelo

    Escolha do modelo com melhor desempenho nos dados de teste e treinamento utilizando o conjunto de treinamento completo.
    Ajuste dos hiperparâmetros do modelo utilizando técnicas como busca em grade ou otimização bayesiana.

## 4. Validação do Modelo

    Avaliação do desempenho do modelo treinado utilizando o conjunto de teste.
    Verificação se o modelo está generalizando bem para novos dados e se não está sofrendo de overfitting.

## 5. Criação dos Pontos de Extremidade

    Implementação de pontos de extremidade para disponibilizar o modelo de previsão.
    Utilização de uma estrutura de API simples para permitir que os usuários enviem novos dados e obtenham previsões de vendas.

## Estrutura do Repositório

    README.md: Este arquivo contendo a descrição do projeto e os passos realizados.
    modelo_previsao_vendas.ipynb: O notebook Jupyter contendo o código utilizado desde a preparação dos dados até o treinamento do modelo.
    pontos_extremidade.json: Arquivo JSON contendo os pontos de extremidade da API para acessar o modelo de previsão.

## Como Usar a API

Para utilizar a API de previsão de vendas, envie uma solicitação POST para o ponto de extremidade fornecido no arquivo JSON. Certifique-se de enviar os dados no formato correto conforme especificado na documentação da API.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.
