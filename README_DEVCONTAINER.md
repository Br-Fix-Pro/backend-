# Guía rápida: Codespaces + Devcontainer + Comandos

## 1) Abrir Codespaces
- Entra a tu repo → Code → Codespaces → Create codespace on main

## 2) Usar el devcontainer
- Este devcontainer instala Python 3.11, Node 20, Docker y extensiones (Copilot, Docker, Python).
- Si te pide recargar, acepta.

## 3) Servicios base
```bash
make infra-up
```
- Postgres (5432), MinIO (9000/9001), MailHog (8025).
- En la pestaña **Ports** podrás abrir los servicios en el navegador.

## 4) Backend (FastAPI)
```bash
make backend-dev
```
- Abre el puerto 8000 y visita `/docs`.

## 5) Inicializar bucket en MinIO (solo primera vez)
```bash
pip install boto3
python scripts/minio_init.py
```

## 6) Web (React)
```bash
make web-dev
```

## 7) Prompts para Copilot Chat (backend)
- Modelos + migraciones (SQLAlchemy/Alembic)
- Endpoints clave (tickets, citas, media, cotización, escrow, firma, etc.)
- Stripe (escrow) + webhooks
- Storage S3 (pre-signed URLs)
- Jobs de recordatorios T-120 y tracking

## 8) Apagar servicios
```bash
make infra-down
```
