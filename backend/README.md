# Docs Scanner - Backend

Backend API for analyzing teaching materials and providing accessibility diagnostics.

## Stack

- Python
- FastAPI
- Uvicorn
- Pydantic

## Run

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the development server:

```bash
uvicorn app.main:app --reload
```

Open http://localhost:8000.

API documentation: http://localhost:8000/docs.

## Structure

```text
app/
  main.py       FastAPI application and initial endpoints

tests/          Backend tests
```

Project documentation and API contracts: `../docs/`.