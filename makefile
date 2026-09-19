UVICORN = uv run uvicorn
ALEMBIC = uv run alembic

run:
	$(UVICORN) main:app --reload

mm:
	$(ALEMBIC) revision --autogenerate -m "$(msg)"

mig:
	$(ALEMBIC) upgrade head
