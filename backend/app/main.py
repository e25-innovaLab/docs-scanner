from fastapi import FastAPI

app = FastAPI(
    title="API de Accesibilidad Docente",
    description="API para el análisis de accesibilidad de materiales educativos.",
    version="0.1.0",
)

@app.get("/")
def root():
    return {
        "message": "Teacher Accessibility API working"
    }

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }