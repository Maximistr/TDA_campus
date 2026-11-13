**[Čeština](#čeština)** · **[English](#english)**

# Čeština

## Začínáme

Prázdná výchozí šablona obsahuje React aplikaci ve `frontend/`, API ve `backend/` a reverzní proxy Caddy pro nasazení na Tour de Cloud.

Lokální vývoj spustíte příkazem:

```bash
docker compose up
```

Frontend běží na `http://localhost:3000`, API na `http://localhost:3001/api/`. Porty 3000, 3001 a 3306 (MySQL) musí být volné. V Docker Desktopu pro macOS nebo Windows zapněte host networking; Linux a OrbStack jej podporují bez nastavování.

## Frontend

Frontend je jednostránková aplikace React/Vite. Hlavní komponenta je `frontend/src/App.jsx`; výchozí stránka je prázdná. Styly jsou v `frontend/src/index.css`.

## Backend

Backend je API ve FastAPI. Endpoint `GET /api/` vrací stav API. Další endpointy můžete přidávat do `backend/app/routes.py`. Připojení k MySQL je nakonfigurované přes proměnné prostředí a databázovou vrstvu v `backend/app/database.py`.

## Nasazení

Push do větve `main` spustí `.github/workflows/deploy.yml` a nasadí projekt na Tour de Cloud. Před prvním nasazením přidejte repository secret `TDC_TOKEN` a v `tourdeapp.yaml` nahraďte `<slug>` slugem svého projektu.

# English

## Getting started

This blank starter template contains a React app in `frontend/`, an API in `backend/`, and a Caddy reverse proxy for Tour de Cloud deployments.

Start local development with:

```bash
docker compose up
```

The frontend is at `http://localhost:3000` and the API is at `http://localhost:3001/api/`. Ports 3000, 3001, and 3306 (MySQL) need to be available. On Docker Desktop for macOS or Windows, enable host networking; Linux and OrbStack support it by default.

## Frontend

The frontend is a React/Vite single-page app. Its main component is `frontend/src/App.jsx`; the starter page is blank. Styles live in `frontend/src/index.css`.

## Backend

The backend is a FastAPI application. `GET /api/` returns the API status. Add endpoints in `backend/app/routes.py`. MySQL connection settings are supplied through environment variables, with the database layer in `backend/app/database.py`.

## Deploying

Pushing to `main` runs `.github/workflows/deploy.yml` and deploys to Tour de Cloud. Before the first deployment, add the `TDC_TOKEN` repository secret and replace `<slug>` in `tourdeapp.yaml` with your project slug.
