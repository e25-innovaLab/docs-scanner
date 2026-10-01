from pydantic import BaseModel


class MaterialResponse(BaseModel):
    id: int
    name: str
    status: str