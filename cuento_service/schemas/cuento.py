from pydantic import BaseModel

class CuentoResponseItem(BaseModel):
    id_cuento: int
    title: str
    text: str
    image: str

    class Config:
        from_attributes = True

class CuentosResponse(BaseModel):
    message: str
    status: int
    data: list[CuentoResponseItem]
