# docs-scanner

Herramienta de accesibilidad para documentos docentes.

## Estructura

```
docs-scanner/
├── frontend/          # Next.js + TypeScript + Tailwind CSS
├── backend/           # FastAPI (próximamente)
├── docs/              # Documentación y evidencia de investigación
└── .github/           # Configuración de la org
```

## Stack

- **Frontend:** Next.js, TypeScript, Tailwind CSS
- **Backend:** FastAPI (Python)
- **IA:** Gemini API

## Getting Started (Frontend)

```bash
cd frontend
npm install
npm run dev
```

Abrí [http://localhost:3000](http://localhost:3000).

## Getting Started (Backend)

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Documentación de la API [http://localhost:8000/docs](http://localhost:8000/docs).

## Licencia

Interno — e25-innovaLab
