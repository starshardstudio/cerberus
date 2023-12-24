#!/usr/bin/env bash
source .env.development
poetry run alembic upgrade head
