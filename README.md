# hello-world — Quote board

A small web app that runs continuously and shows inspirational quotes. All quotes live in [`quotes.py`](quotes.py); the app does not call external APIs.

## Run with Docker

```bash
docker build -t hello-world-quotes .
docker run --rm -p 8080:8080 hello-world-quotes
```

Open [http://localhost:8080](http://localhost:8080).

## Run locally (optional)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Endpoints

| Path | Description |
|------|-------------|
| `/` | Quote board UI |
| `/health` | Liveness check |
| `/api/quotes` | JSON list of all quotes |
| `/api/quotes/random` | One random quote (JSON) |
