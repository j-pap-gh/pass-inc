import pytest
from fastapi.testclient import TestClient

from src.pass_inc.main import create_app

@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)

def test_signup_and_login(client):
    # sign up user
    resp = client.post("/auth/signup", json={"email": "user1@example.com", "password": "password123"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["email"] == "user1@example.com"
    # login to get token
    resp = client.post("/auth/login", data={"username": "user1@example.com", "password": "password123"})
    assert resp.status_code == 200
    token_data = resp.json()
    assert "access_token" in token_data
    assert token_data["token_type"] == "bearer"
