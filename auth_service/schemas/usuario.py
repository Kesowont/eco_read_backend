from pydantic import BaseModel

class UsuarioBase(BaseModel):
    nombre: str
    clave: str

class UsuarioResponse(BaseModel):
    id_usuario: int
    nombre: str
    edad: int

    class Config:
        from_attributes = True

class UsuarioCreate(UsuarioBase):
    edad: int

    class Config:
        from_attributes = True
