from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.material import MaterialResponse
from app.services.material_service import create_material


router = APIRouter(
    prefix="/materials",
    tags=["Materials"],
)


@router.post(
    "",
    response_model=MaterialResponse,
    status_code=201,
)
def upload_material(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
):
    return create_material(
        db=db,
        file=file,
    )