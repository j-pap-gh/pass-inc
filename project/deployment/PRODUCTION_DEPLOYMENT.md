
# 🚀 Production Deployment Guide — Passive Income Platform

## Backend (FastAPI)

### Local Development
```
cd backend
uvicorn app.main:app --reload
```

### Docker
```
cd backend
docker build -t passive-api .
docker run -p 8000:8000 --env-file .env passive-api
```

### Render Deployment
1. Push the repo to GitHub.
2. Create a new Web Service in Render.
3. Build command:
   ```
   pip install -r requirements.txt
   ```
4. Start command:
   ```
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```
5. Set environment variables using `.env.example`.

---

## Frontend (Vite + React)

### Local Development
```
cd frontend
npm install
npm run dev
```

### Build for Production
```
npm run build
```

### Vercel Deployment
- Connect repo to Vercel or use `vercel` CLI.

### Netlify Deployment
- Use `netlify.toml`.
- Supports SPA routing out of the box.

---

## Stripe Integration

Webhook endpoint:
```
POST /subscribe/webhook
```

You must set:
- `STRIPE_SECRET_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `PREMIUM_PRICE_ID`

---

## Alembic Migrations

Apply database migrations:

```
cd backend
alembic upgrade head
```

This will run:
- `0001_init`
- `0002_add_ideas_fields`
- `0003_add_premium_field`

---

## AI Chat

AI service located at:
```
backend/app/services/ai_service.py
```

Replace stub with an OpenAI call using your `OPENAI_API_KEY`.

---

## Environment Variables

Copy `.env.example` → `.env` and fill in real secrets.
