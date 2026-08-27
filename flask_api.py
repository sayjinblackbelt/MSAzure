from flask import Flask, jsonify, request
import os
import joblib
import numpy as np

app = Flask(__name__)

MODEL_PATH = os.getenv("MODEL_PATH", "model/vendas_model.pkl")


def load_model():
    if not os.path.exists(MODEL_PATH):
        return None
    return joblib.load(MODEL_PATH)


@app.get("/")
def home():
    return jsonify({
        "projeto": "Previsão de Vendas com Azure Machine Learning e Flask",
        "status": "online",
        "endpoint": "POST /prever_vendas"
    })


@app.post("/prever_vendas")
def prever_vendas():
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({"erro": "Envie os dados em formato JSON."}), 400

    campos = ["preco", "promocao", "quantidade", "tipo_produto"]
    ausentes = [campo for campo in campos if campo not in dados]

    if ausentes:
        return jsonify({
            "erro": "Campos obrigatórios ausentes.",
            "campos_ausentes": ausentes
        }), 400

    try:
        preco = float(dados["preco"])
        promocao = int(bool(dados["promocao"]))
        quantidade = float(dados["quantidade"])
        tipo_produto = str(dados["tipo_produto"])
    except (TypeError, ValueError):
        return jsonify({"erro": "Valores de entrada inválidos."}), 400

    model = load_model()

    if model is None:
        return jsonify({
            "erro": "Modelo não encontrado.",
            "detalhe": f"Arquivo esperado: {MODEL_PATH}",
            "status": "modelo_nao_disponivel"
        }), 503

    try:
        # O modelo deve receber as mesmas variáveis e transformações
        # utilizadas durante o treinamento.
        entrada = np.array([[preco, promocao, quantidade, tipo_produto]], dtype=object)
        previsao = model.predict(entrada)[0]

        return jsonify({
            "previsao_vendas": float(previsao)
        })
    except Exception as exc:
        return jsonify({
            "erro": "Não foi possível realizar a previsão.",
            "detalhe": str(exc)
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=False)
