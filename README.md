# Library Management API

This is a FastAPI application for basic library management (users, books, borrow/return).

## Quick start (local)

1. Create a virtual environment and install dependencies:

```bash
python -m venv .venv
source .venv/bin/activate   # PowerShell: .venv\Scripts\Activate
python -m pip install -r requirements.txt
```

2. Run locally:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Open `http://127.0.0.1:8000/docs` for the interactive API docs.

## Docker

Build and run with Docker:

```bash
docker build -t library-management .
docker run -p 8000:8000 library-management
```

The container will run `uvicorn main:app` and expose port `8000`. You may pass a `PORT` env var to override the port.

## Deploy to Render (Docker)

1. Push this repository to GitHub.
2. Create a new Web Service on Render and connect your GitHub repo.
3. Choose "Docker" as the environment (Render will use the `Dockerfile`).
4. Set the service to use `web` and ensure the service's port is `8000` (Render sets `$PORT` automatically).
5. Deploy — Render will build the Docker image and run it.

Notes:
- The app uses SQLite (`library.db`) by default. For production use, switch to a managed DB (Postgres/MySQL) and update `database.py` accordingly.
- Add any environment variables via Render's dashboard (for example, `DATABASE_URL` if you change the DB backend).

## Deploy to Heroku (optional)

1. Login with the Heroku CLI and create an app.
2. Ensure the `Procfile` is present (this repo contains one).
3. Push to Heroku (either via Git or GitHub integration). Heroku will install requirements and run the `web` command from the `Procfile`.

## Production considerations

- Replace SQLite with a managed database and update `database.py`.
- Add proper secrets management and don't store sensitive config in the repo.
- Consider using a process manager (Gunicorn + UvicornWorkers) for high-load environments.

