import pytest

from flask_api import app


@pytest.fixture
def client():
    app.config.update(TESTING=True)
    with app.test_client() as client:
        yield client


def test_prever_vendas_dados_validos(client):
    response = client.post(
        "/prever_vendas",
        json={
            "preco": 20.50,
            "promocao": True,
            "quantidade": 100,
            "tipo_produto": "eletronico",
        },
    )

    assert response.status_code == 200
    data = response.get_json()
    assert "previsao_vendas" in data
    assert isinstance(data["previsao_vendas"], (int, float))


def test_prever_vendas_campo_ausente(client):
    response = client.post(
        "/prever_vendas",
        json={
            "preco": 20.50,
            "promocao": True,
            "quantidade": 100,
        },
    )

    assert response.status_code == 400
    data = response.get_json()
    assert data["erro"] == "Campos obrigatórios ausentes."
    assert "tipo_produto" in data["campos_ausentes"]


def test_prever_vendas_valor_invalido(client):
    response = client.post(
        "/prever_vendas",
        json={
            "preco": "vinte",
            "promocao": True,
            "quantidade": 100,
            "tipo_produto": "eletronico",
        },
    )

    assert response.status_code == 400
    assert response.get_json()["erro"] == "Valores de entrada inválidos."
