# Fix‑Pro / E3 — Monorepo

Este monorepo contiene:
- `backend/` (FastAPI)
- `web-app/` (React)
- `mobile-app/` (Flutter)
- `infra/` (docker-compose, k8s/terraform opcional)
- `docs/` (backlog, diagramas, decisiones)

## Primeros pasos
1) Clona el repo y copia `.env.example` a `.env` en cada paquete.
2) Levanta servicios locales: `cd infra && docker compose up -d`.
3) Arranca el backend: `cd backend && pip install -r requirements.txt && uvicorn app.main:app --reload`.
4) Arranca el front web: `cd web-app && npm install && npm run dev`.
5) (Opcional) Crea el proyecto Flutter y apunta `API_BASE` al backend.
6) Sube tus PDFs/diagramas a `docs/`.

## Convenciones
- Branches: `feat/*`, `fix/*`, `chore/*`
- Commits: Conventional Commits
- PRs con checklist (tests, lint, docs)
- CI: `.github/workflows/`

## Seguridad
- Nunca subas `.env` con secretos.
- Usa GitHub Secrets para despliegues.
- Habilita MFA en la organización.
