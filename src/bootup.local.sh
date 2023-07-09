#!/bin/sh

# database migration
alembic upgrade head

# app startup
uvicorn main:app --host "0.0.0.0" --port 8000 --reload