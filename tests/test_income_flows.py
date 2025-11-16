from fastapi.testclient import TestClient

from src.pass_inc.main import app

client = TestClient(app)


def test_create_and_summarize_income():
    # create income stream
    payload = {
        "name": "Dividend portfolio",
        "income_type": "dividend",
        "amount_per_period": 100.0,
        "period": "monthly",
        "currency": "USD",
    }
    res = client.post("/income/", json=payload)
    assert res.status_code == 201
    stream = res.json()
    assert stream["name"] == payload["name"]

    # get summary
    summary_res = client.get("/income/summary")
    assert summary_res.status_code == 200
    summary = summary_res.json()
    assert summary["total_monthly"] >= 100.0
    assert summary["total_yearly"] >= 1200.0
