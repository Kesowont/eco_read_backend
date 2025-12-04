from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from cuento_service.models.cuento import Cuento
from cuento_service.database import get_db
from cuento_service.schemas.cuento import CuentosResponse

router = APIRouter()

@router.get("/v1/cuento/listar/{id_usuario}", response_model=CuentosResponse)
def listar_cuentos(id_usuario: int, db: Session = Depends(get_db)):
    # Aquí podrías filtrar cuentos por el usuario si fuera necesario.
    cuentos = db.query(Cuento).all()

    return {
        "message": "Cuentos obtenidos correctamente",
        "status": 200,
        "data": cuentos
    }
