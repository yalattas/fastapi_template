# fastAPI template

## component
1. FastAPI
2. SQLAlchemy ORM - postgres
3. alembic - migrations

### FastAPI
```
docker compose up -d --build && docker compose logs -f
```

### alembic
1. browse migration history
```
docker compose exec -it backend.ai.app.svc.local alembic history --verbose 
```
2. create a migration plan
```
docker compose exec -it backend.ai.app.svc.local alembic revision --autogenerate -m "COMMENT GOES HERE"
```
3. create a manual revision
```
docker compose exec -it backend.ai.app.svc.local alembic revision 
```
