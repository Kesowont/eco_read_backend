from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from respuesta_service.models.respuesta import Control
from respuesta_service.schemas.respuesta import ResponderRequest, ResponderResponse
from preguntas_service.models.pregunta import Pregunta

router = APIRouter()


@router.post("/v1/responder", response_model=ResponderResponse)
def responder(request: ResponderRequest, db: Session = Depends(get_db)):
    # parse respuestas: accept comma-separated string
    respuestas = [r.strip().lower() for r in request.array_respuestas.split(",") if r.strip() != ""]

    preguntas = db.query(Pregunta).filter(Pregunta.id_cuento == request.id_cuento).order_by(Pregunta.id_pregunta).all()

    if not preguntas:
        raise HTTPException(status_code=404, detail="No se encontraron preguntas para este cuento")

    total = len(preguntas)
    # if number of provided answers doesn't match, allow missing answers but compare up to min length
    compare_len = min(len(respuestas), total)

    detalle = {}
    correct = 0
    for i in range(total):
        expected = (preguntas[i].resp_correcta or "").strip().lower()
        given = respuestas[i] if i < compare_len else ""
        is_correct = (given == expected)
        detalle[preguntas[i].id_pregunta] = is_correct
        if is_correct:
            correct += 1

    # compute estrella as 0-5 scale based on percent correct
    if total == 0:
        estrella = 0
    else:
        pct = correct / total
        estrella = int(round(pct * 5))

    # save or update control: if a control exists for this user+cuento, update estrella
    existing = db.query(Control).filter(
        Control.id_usuario == request.id_usuario,
        Control.id_cuento == request.id_cuento,
    ).first()

    existing.estrella = estrella
    db.commit()
    db.refresh(existing)


    data = {
        "total": total,
        "correct": correct,
        "estrella": estrella,
        "detalle": detalle,
    }

    return {
        "message": "Respuestas procesadas",
        "status": 200,
        "data": data,
    }