from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from preguntas_service.models.pregunta import Pregunta
from preguntas_service.database import get_db
from preguntas_service.schemas.pregunta import PreguntasResponse

router = APIRouter()

@router.get("/v1/cuento/preguntas/{id_cuento}", response_model=PreguntasResponse)
def listar_preguntas(id_cuento: int, db: Session = Depends(get_db)):

    # Filtrar por cuento
    preguntas = db.query(Pregunta).filter(Pregunta.id_cuento == id_cuento).all()

    if not preguntas:
        raise HTTPException(
            status_code=404,
            detail=f"No se encontraron preguntas para el cuento con id {id_cuento}"
        )

    return {
        "message": "Preguntas obtenidas correctamente",
        "status": 200,
        "data": preguntas
    }
