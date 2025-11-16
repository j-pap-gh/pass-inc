# pass-inc

Passive income tracker SaaS-style backend with recommendations.

This is the backend service for tracking passive income streams (dividends, rentals, royalties,
etc.) and generating basic recommendations. Future plans include AI-powered insights and
paywalled advanced strategies.

## Requirements

- Python 3.10+
- pip

## Setup

```bash
git clone https://github.com/j-pap-gh/pass-inc.git
cd pass-inc

# (optional) create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# install dependencies
pip install -r requirements.txt
```

## Running the API

```bash
uvicorn src.pass_inc.main:app --reload
```

By default FastAPI will serve at [http://localhost:8000](http://localhost:8000).

Open the interactive docs:

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

## Key endpoints

- `GET /health` – basic health check
- `GET /income/` – list income streams
- `POST /income/` – create a new income stream
- `DELETE /income/{stream_id}` – delete a stream
- `GET /income/summary` – monthly/yearly totals
- `GET /recommendations/` – baseline recommendations
- `GET /recommendations/paywalled-preview` – example of paywalled recommendation preview

## Running tests

```bash
pytest
```

## Next steps / roadmap

- Persist data in a real database (e.g. Postgres with SQLAlchemy).
- User accounts, authentication, and subscription tiers.
- AI-based recommendation engine gated behind a paid plan.
- Frontend (web dashboard) that consumes this API.
