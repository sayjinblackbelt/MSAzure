"""Treinamento do modelo de previsão de vendas.

Este script pode ser executado localmente ou adaptado para um job do
Azure Machine Learning. O modelo é salvo em model/vendas_model.pkl.
"""

from pathlib import Path

import joblib
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

DATA_PATH = Path("data/vendas.csv")
MODEL_PATH = Path("model/vendas_model.pkl")

FEATURES = ["preco", "promocao", "quantidade", "tipo_produto"]
TARGET = "vendas"


def criar_dados_exemplo() -> pd.DataFrame:
    """Cria um pequeno dataset demonstrativo para testar o pipeline."""
    return pd.DataFrame([
        {"preco": 20.50, "promocao": True, "quantidade": 100, "tipo_produto": "eletronico", "vendas": 82},
        {"preco": 35.00, "promocao": False, "quantidade": 80, "tipo_produto": "eletronico", "vendas": 48},
        {"preco": 15.00, "promocao": True, "quantidade": 120, "tipo_produto": "casa", "vendas": 91},
        {"preco": 50.00, "promocao": False, "quantidade": 60, "tipo_produto": "casa", "vendas": 31},
        {"preco": 12.50, "promocao": True, "quantidade": 150, "tipo_produto": "papelaria", "vendas": 115},
        {"preco": 28.00, "promocao": True, "quantidade": 90, "tipo_produto": "papelaria", "vendas": 70},
        {"preco": 42.00, "promocao": False, "quantidade": 75, "tipo_produto": "eletronico", "vendas": 39},
        {"preco": 18.00, "promocao": True, "quantidade": 130, "tipo_produto": "casa", "vendas": 98},
        {"preco": 25.00, "promocao": False, "quantidade": 100, "tipo_produto": "papelaria", "vendas": 55},
        {"preco": 10.00, "promocao": True, "quantidade": 160, "tipo_produto": "papelaria", "vendas": 128},
    ])


def carregar_dados() -> pd.DataFrame:
    if DATA_PATH.exists():
        return pd.read_csv(DATA_PATH)

    print(f"Dataset não encontrado em {DATA_PATH}. Usando dados demonstrativos.")
    return criar_dados_exemplo()


def construir_pipeline() -> Pipeline:
    numericas = ["preco", "promocao", "quantidade"]
    categoricas = ["tipo_produto"]

    preprocessor = ColumnTransformer([
        ("num", SimpleImputer(strategy="median"), numericas),
        ("cat", Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore")),
        ]), categoricas),
    ])

    return Pipeline([
        ("preprocessamento", preprocessor),
        ("modelo", RandomForestRegressor(
            n_estimators=200,
            random_state=42,
            min_samples_leaf=1,
        )),
    ])


def main() -> None:
    df = carregar_dados()

    faltantes = [col for col in FEATURES + [TARGET] if col not in df.columns]
    if faltantes:
        raise ValueError(f"Colunas obrigatórias ausentes: {faltantes}")

    X = df[FEATURES].copy()
    y = pd.to_numeric(df[TARGET], errors="raise")

    X["promocao"] = X["promocao"].astype(bool)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    pipeline = construir_pipeline()
    pipeline.fit(X_train, y_train)

    previsoes = pipeline.predict(X_test)
    rmse = mean_squared_error(y_test, previsoes) ** 0.5
    r2 = r2_score(y_test, previsoes)

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)

    print(f"RMSE: {rmse:.4f}")
    print(f"R²: {r2:.4f}")
    print(f"Modelo salvo em: {MODEL_PATH}")


if __name__ == "__main__":
    main()
