# Previsão de Vendas com Azure Machine Learning e Flask

Projeto de estudo e demonstração de **Machine Learning aplicado à previsão de vendas**, combinando Python, scikit-learn, Azure Machine Learning e Flask.

## Objetivo

Construir um fluxo completo de Machine Learning capaz de:

1. Preparar dados históricos de vendas;
2. Aplicar pré-processamento às variáveis;
3. Treinar e avaliar um modelo de regressão;
4. Salvar e versionar o modelo treinado;
5. Disponibilizar previsões por meio de uma API REST com Flask;
6. Preparar o projeto para posterior execução no Azure Machine Learning.

## Arquitetura

```text
Dataset CSV
    │
    ▼
Pré-processamento
    │
    ▼
Treinamento / Avaliação
    │
    ▼
Modelo scikit-learn
    │
    ├── Execução local
    │
    └── Azure Machine Learning
    │
    ▼
Modelo serializado
    │
    ▼
Flask API
    │
    ▼
POST /prever_vendas
    │
    ▼
Previsão
```

## Estrutura do Repositório

```text
MSAzure/
├── README.md
├── .gitignore
├── azure_ml_training.py
├── flask_api.py
├── requirements.txt
├── data/
│   └── vendas.csv
└── model/
    └── vendas_model.pkl   # gerado localmente, não versionado
```

| Arquivo | Descrição |
|---|---|
| `README.md` | Documentação do projeto. |
| `azure_ml_training.py` | Pipeline de preparação, treinamento e avaliação do modelo. |
| `flask_api.py` | API Flask para disponibilizar as previsões. |
| `requirements.txt` | Dependências Python. |
| `data/vendas.csv` | Dataset demonstrativo utilizado no treinamento. |
| `model/vendas_model.pkl` | Modelo serializado gerado após o treinamento. |
| `.gitignore` | Arquivos locais que não devem ser versionados. |

## Dados

O dataset demonstrativo possui as seguintes variáveis:

- `preco`: preço do produto;
- `promocao`: indica se o produto está em promoção;
- `quantidade`: quantidade disponível/ofertada;
- `tipo_produto`: categoria do produto;
- `vendas`: variável-alvo que o modelo deve prever.

Os dados presentes no repositório são **demonstrativos** e têm finalidade educacional. Para um projeto real, o dataset deve ser substituído por dados históricos confiáveis e adequadamente documentados.

## Modelo de Machine Learning

O pipeline utiliza `scikit-learn` e `RandomForestRegressor`.

O pré-processamento inclui:

- imputação de valores ausentes;
- tratamento de variáveis numéricas;
- codificação One-Hot da variável categórica `tipo_produto`;
- divisão entre dados de treinamento e teste.

As métricas utilizadas são:

- **RMSE** — Root Mean Squared Error;
- **R²** — Coeficiente de Determinação.

O pipeline completo é serializado com `joblib`, permitindo que a API Flask utilize exatamente o mesmo pré-processamento aplicado durante o treinamento.

## Treinamento Local

### 1. Clonar o repositório

```bash
git clone https://github.com/sayjinblackbelt/MSAzure.git
cd MSAzure
```

### 2. Criar ambiente virtual

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

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Treinar o modelo

```bash
python azure_ml_training.py
```

Ao final, o script apresenta RMSE e R² e gera:

```text
model/vendas_model.pkl
```

## Flask API

Depois de treinar o modelo, execute:

```bash
python flask_api.py
```

A API estará disponível em:

```text
http://localhost:5000
```

### Endpoint de saúde

```text
GET /
```

### Endpoint de previsão

```text
POST /prever_vendas
```

Exemplo de requisição:

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

Resposta esperada:

```json
{
    "previsao_vendas": 80.0
}
```

O valor acima é apenas ilustrativo; a previsão real depende do modelo treinado.

## Azure Machine Learning

A implementação atual possui um pipeline Python que pode servir como base para execução em um ambiente Azure Machine Learning.

O próximo estágio da integração deverá contemplar:

1. criação/configuração do workspace;
2. conexão do ambiente Python ao Azure ML;
3. upload ou registro do dataset;
4. execução do treinamento como job;
5. registro do modelo no Azure ML Model Registry;
6. definição de um ambiente de execução reproduzível;
7. implantação do modelo como endpoint gerenciado ou integração com a API.

> Importante: credenciais, chaves, connection strings e outros segredos não devem ser armazenados no GitHub.

## Teste rápido da API

Com a API em execução:

```bash
curl -X POST http://localhost:5000/prever_vendas ^
  -H "Content-Type: application/json" ^
  -d "{\"preco\":20.50,\"promocao\":true,\"quantidade\":100,\"tipo_produto\":\"eletronico\"}"
```

No Linux/macOS, use `\` no lugar de `^` para continuação de linha.

## Tecnologias

- Python 3
- pandas
- NumPy
- scikit-learn
- joblib
- Flask
- requests
- Jupyter Notebook
- Azure Machine Learning

## Status

**Em desenvolvimento — pipeline local funcional e integração com Azure ML em evolução.**

### Concluído

- [x] Dataset demonstrativo;
- [x] Pipeline de pré-processamento;
- [x] Modelo Random Forest;
- [x] Avaliação com RMSE e R²;
- [x] Serialização do pipeline com joblib;
- [x] API Flask;
- [x] Validação básica das entradas da API;
- [x] Documentação inicial;
- [x] `.gitignore`.

### Próximas etapas

- [ ] Criar notebook `.ipynb` equivalente ao pipeline;
- [ ] Criar testes automatizados da API;
- [ ] Comparar Random Forest com Regressão Linear;
- [ ] Melhorar o dataset e aumentar o volume de dados;
- [ ] Executar treinamento no Azure Machine Learning;
- [ ] Registrar o modelo no Azure ML;
- [ ] Criar endpoint de inferência no Azure;
- [ ] Documentar métricas e experimentos;
- [ ] Criar CI/CD posteriormente.

## Licença

Este projeto está licenciado sob a **MIT License**.

---

## Author

**Filipe G Morais**

GitHub: https://github.com/sayjinblackbelt  
Repository: https://github.com/sayjinblackbelt/MSAzure
