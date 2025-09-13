    .PHONY: infra-up infra-down backend-dev web-dev mobile-dev

    infra-up:
	cd infra && cp -n .env.example .env || true && docker compose up -d

    infra-down:
	cd infra && docker compose down

    backend-dev:
	cd backend && cp -n .env.example .env || true && pip install -r requirements.txt && uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

    web-dev:
	cd web-app && cp -n .env.example .env || true && npm install && npm run dev

    mobile-dev:
	@echo "Open mobile-app/ and run your Flutter commands (flutter create, flutter run)."
