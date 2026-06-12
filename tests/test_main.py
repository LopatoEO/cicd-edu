from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


def test_root_returns_hello_world():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_app_not_found():
    response = client.get("/app")

    assert response.status_code == 404

def test_app_title_is_configured():
    assert "FastAPI application" in app.title
