# Reverse Job Board API

This project provides a basic API for a reverse job board built with [FastAPI](https://fastapi.tiangolo.com/). It exposes endpoints to manage users and notifications and includes models for companies, job postings and applications.

## Features

- **User management**: create, update, delete and authenticate users with JWT tokens.
- **Notifications**: create and list notifications for users or companies.
- **SQLAlchemy models**: users, companies, postings, applications and more.
- **SQLite database** by default for quick local development.
- **Automated tests** using `pytest`.

## Requirements

- Python 3.11+
- The packages listed in `requirements.txt`

## Installation

```bash
# clone the repository and change to the project directory
pip install -r requirements.txt
```

## Running the application

Execute the helper script in `cli/run.py` which runs `uvicorn` with hot reload:

```bash
python cli/run.py
```

The API will be available at `http://127.0.0.1:8000`. Interactive documentation is provided at `/docs`.

## Running the tests

```
pytest
```

## Configuration

The application reads configuration values such as token secrets from environment variables. Default values are defined in `app/core/config.py` and can be overridden using a `.env` file.

## Project structure

```
app/            # FastAPI application
  core/         # configuration and security utilities
  db/           # database models and session
  models/       # SQLAlchemy models
  routes/       # API routes
  schemas/      # Pydantic schemas
  services/     # business logic
cli/            # helper scripts
tests/          # pytest suite
```

Feel free to modify or extend this project to suit your needs.
