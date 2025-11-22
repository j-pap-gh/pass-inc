import pytest
from fastapi.testclient import TestClient
from src.pass_inc.main import create_app

@pytest.fixture
def client():
    app = create_app()
    return TestClient(app)

def authenticate(client, email, password):
    client.post("/auth/signup", json={"email": email, "password": password})
    res = client.post("/auth/login", data={"username": email, "password": password})
    token = res.json()["access_token"]
    return {"Authorization": f"Bearer {token}"}

def test_create_list_update_delete_income(client):
    headers1 = authenticate(client, "alice@example.com", "password1")
    payload = {
        "name": "Job",
        "income_type": "BUSINESS",
        "amount_per_period": 1000.0,
        "period": "monthly",
        "currency": "USD",
        "start_date": "2025-01-01",
        "notes": "Test"
    }
    res = client.post("/income/", json=payload, headers=headers1)
    assert res.status_code == 201
    income = res.json()
    income_id = income["id"]
    assert income["name"] == "Job"
    res = client.get("/income/", headers=headers1)
    assert len(res.json()) >= 1
    new_payload = payload.copy()
    new_payload["name"] = "Updated Job"
    res = client.put(f"/income/{income_id}", json=new_payload, headers=headers1)
    assert res.status_code == 200
    assert res.json()["name"] == "Updated Job"
    res = client.delete(f"/income/{income_id}", headers=headers1)
    assert res.status_code == 204
    res = client.get("/income/", headers=headers1)
    assert all(item["id"] != income_id for item in res.json())
    res2 = client.post("/income/", json=payload, headers=headers1)
    income2_id = res2.json()["id"]
    headers2 = authenticate(client, "bob@example.com", "password2")
    res = client.delete(f"/income/{income2_id}", headers=headers2)
    assert res.status_code == 404
