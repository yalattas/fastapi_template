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
# KeyCloak
## initial setup
1. visit `iam-backend` endpoint and create your first `realm` instance at [http://localhost:8080/admin](http://localhost:8080/admin)
> use the environment variables of admin credentials or ask the administrator
2. after creating the `realm`. from the left side menu, go To `clients` -> create a client -> name your client and mark down your `Client ID`
3. visit your created `relam` -> `settings` -> activate `user authentication` and select `service accounts role` OR activate `Authorization`
4. on the same page, visit `credentials` and save `Client Secret` and copy the secret, then put it in `settings.py` -> `CLIENT_SECRET_KEY`
5. `client-role` in `settings.py` should be same as follows`client-role` OR look for the name in the client `Roles` tab
6. in `client` page, visit `Service account role` tab and assign a role `manage-users`

## cli token
```
curl --location --request POST 'http://localhost:8080/realms/main/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=password' \
--data-urlencode 'client_id=backend_service' \
--data-urlencode 'client_secret=CLIENT_SECRET' \
--data-urlencode 'username=test' \
--data-urlencode 'password=123' \
--data-urlencode 'realm=main' \
--data-urlencode 'scope=openid'
```