install:
	poetry add ${LIB}

remove:
	poetry remove ${LIB}

run:
	poetry run uvicorn app.main:app --host localhost --port 8000 --reload

migrate-create:
	alembic revision --autogenerate -m ${MIGRATION}

migrate-apply:
	alembic upgrade head