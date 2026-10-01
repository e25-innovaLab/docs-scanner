from fastapi import FastAPI

from app.routers.materials import router as materials_router


app = FastAPI(
    title="API de Accesibilidad Docente",
    description="API para el análisis de accesibilidad de materiales educativos.",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }


app.include_router(materials_router)