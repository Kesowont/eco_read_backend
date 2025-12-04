from pydantic import BaseModel

class PreguntasResponseItem(BaseModel):
    id_pregunta: int
    contenido: str

    class Config:
        from_attributes = True

class PreguntasResponse(BaseModel):
    message: str
    status: int
    data: list[PreguntasResponseItem]
