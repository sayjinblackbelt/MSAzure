# Previsão de Vendas com Azure Machine Learning e Flask

Projeto de estudo e demonstração de **Machine Learning aplicado à previsão de vendas**, combinando **Azure Machine Learning** para preparação e treinamento do modelo com **Flask** para disponibilização das previsões por meio de uma API REST.

## Objetivo

Construir um fluxo completo de Machine Learning capaz de:

1. Preparar dados históricos de vendas e características dos produtos;
2. Treinar e avaliar um modelo de regressão;
3. Registrar o modelo no Azure Machine Learning;
4. Disponibilizar o modelo por meio de uma API Flask;
5. Receber dados de entrada e retornar uma previsão de vendas.

## Arquitetura

```text
Dados de vendas
      │
      ▼
Preparação dos dados
      │
      ▼
Azure Machine Learning
      │
      ├── Treinamento
      ├── Avaliação
      └── Registro do modelo
              │
              ▼
         Modelo treinado
              │
              ▼
          Flask API
              │
              ▼
       Requisição POST
              │
              ▼
       Previsão de vendas
```

## Azure Machine Learning

O Azure Machine Learning é utilizado como ambiente para preparação dos dados, treinamento, avaliação e registro do modelo.

### Preparação dos Dados

As etapas de pré-processamento podem incluir tratamento de valores ausentes, identificação de inconsistências, codificação de variáveis categóricas, normalização ou padronização quando necessária e separação dos dados em conjuntos de treinamento e teste.

### Treinamento do Modelo

O projeto pode utilizar modelos de regressão adequados ao conjunto de dados, como **Regressão Linear** e **Random Forest Regressor**.

O desempenho deve ser analisado utilizando métricas apropriadas, como **RMSE (Root Mean Squared Error)** e **R² (Coeficiente de Determinação)**.

### Registro do Modelo

Após o treinamento e a avaliação, o modelo pode ser registrado no Azure Machine Learning para facilitar seu versionamento, gerenciamento e posterior implantação.

## Flask API

A API Flask funciona como camada de acesso ao modelo, permitindo que aplicações externas enviem os dados necessários para uma previsão.

### Endpoint

```text
POST /prever_vendas
```

### Exemplo de Requisição

```python
import requests

url = "http://localhost:5000/prever_vendas"

dados = {
    "preco": 20.50,
    "promocao": True,
    "quantidade": 100,
    "tipo_produto": "eletronico"
}

resposta = requests.post(url, json=dados)
print(resposta.json())
```

> Os campos apresentados são um exemplo de contrato da API. Eles devem ser ajustados de acordo com as variáveis efetivamente utilizadas pelo modelo treinado.

## Estrutura do Repositório

```text
MSAzure/
├── README.md
├── azure_ml_training.ipynb
├── flask_api.py
└── requirements.txt
```

| Arquivo | Descrição |
|---|---|
| `README.md` | Documentação do projeto. |
| `azure_ml_training.ipynb` | Notebook para preparação dos dados, treinamento e avaliação do modelo. |
| `flask_api.py` | Código da API Flask responsável por disponibilizar as previsões. |
| `requirements.txt` | Dependências Python necessárias para execução do projeto. |

## Como Executar Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/sayjinblackbelt/MSAzure.git
cd MSAzure
```

### 2. Criar um ambiente virtual

```bash
python -m venv .venv
```

No Windows:

```bash
.venv\Scripts\activate
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a API

```bash
python flask_api.py
```

A API ficará disponível, conforme a configuração do Flask, em `http://localhost:5000`.

## Tecnologias

- Python
- Jupyter Notebook
- Azure Machine Learning
- Flask
- scikit-learn
- pandas
- requests

## Status

**Em desenvolvimento.**

O repositório documenta a proposta e a estrutura do projeto. A implementação efetiva do notebook, do modelo treinado, da API e do processo de implantação deve ser mantida versionada no próprio repositório conforme o desenvolvimento avançar.

## Próximas Etapas

- [ ] Adicionar o notebook de treinamento;
- [ ] Definir e versionar o conjunto de dados utilizado;
- [ ] Implementar o pipeline de pré-processamento;
- [ ] Treinar e comparar modelos de regressão;
- [ ] Registrar o modelo no Azure Machine Learning;
- [ ] Implementar a API Flask;
- [ ] Criar testes para o endpoint de previsão;
- [ ] Documentar o contrato da API;
- [ ] Avaliar implantação do serviço.

## Contribuições

Contribuições são bem-vindas. Sugestões, correções e melhorias podem ser propostas por meio de **Issues** e **Pull Requests**.

## Licença

Este projeto está licenciado sob a **MIT License**.
