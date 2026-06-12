from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root_returns_hello_world():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_app_title_is_configured():
    assert "FastAPI application" in app.title

def test_multiply():
    response = client.get("/actions/multiply?a=3&b=4")

    assert response.status_code == 200
    assert response.json() == {"result": 12}
