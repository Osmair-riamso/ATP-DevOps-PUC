# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_item():
    response = client.post("/items/", json={"name": "Test Item", "price": 10.0})
    assert response.status_code == 200
    assert response.json() == {"name": "Test Item", "price": 10.0}

def test_read_items():
    response = client.get("/items/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
