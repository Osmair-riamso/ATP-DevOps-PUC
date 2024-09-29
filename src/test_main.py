from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

# Teste para o endpoint raiz "/"
def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Olá Mundo"}

# Teste para o endpoint "/funcaoteste"
def test_funcaoteste():
    response = client.get("/funcaoteste")
    assert response.status_code == 200
    # Verifique se o campo "funcaoteste" é True
    assert response.json()["funcaoteste"] is True
    # Verifique se o número aleatório está dentro do intervalo esperado
    assert 0 <= response.json()["num_alatorio"] <= 20000

# Teste para o POST de estudante "/estudantes/cadastro"
def test_create_estudante():
    response = client.post("/estudantes/cadastro", json={"nome": "Jo", "curso": "TI", "ativo": True})
    assert response.status_code == 200
    assert response.json() == {"nome": "Jo", "curso": "TI", "ativo": True}

# Teste para o PUT de estudante "/estudantes/update/{id_estudante}"
def test_update_estudante():
    response = client.put("/estudantes/update/1")
    assert response.status_code == 200
    assert response.json() is True  # Verifica que o ID é maior que 0

# Teste para o DELETE de estudante "/estudantes/delete/{id_estudante}"
def test_delete_estudante():
    response = client.delete("/estudantes/delete/1")
    assert response.status_code == 200
    assert response.json() is True  # Verifica que o ID é maior que 0
