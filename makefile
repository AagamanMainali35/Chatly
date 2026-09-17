UVICORN = uv run uvicorn

run:
	$(UVICORN) main:app --reload
