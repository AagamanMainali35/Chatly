UVICORN = uv run uvicorn
ALEMBIC = uv run alembic

run:
	$(UVICORN) main:app --reload

mm:
	$(ALEMBIC) revision --autogenerate -m "$(msg)"

mig:
	$(ALEMBIC) upgrade head

rollback:
	$(ALEMBIC) downgrade -1

migration-history:
	$(ALEMBIC) history

migration-current:
	$(ALEMBIC) current

commit:
	GIT_AUTHOR_DATE="$(DATE)" GIT_COMMITTER_DATE="$(DATE)" git commit -m "$(MESSAGE)"