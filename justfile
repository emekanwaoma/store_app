format:
	black . --preview
	ruff . --fix

install:
	pip install -r requirements.txt

lint:
	black . --preview
	ruff . --check

pre_commit:
	just format

start_local:
	docker compose up --build

down_local:
	docker compose -f docker-compose-local.yml down
	
start:
	docker compose docker-compose.prod.yml up -d --build

down:
	docker compose -f docker-compose-local.yml down

