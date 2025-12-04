from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# IMPORTAS LOS ROUTERS DE CADA SERVICIO
from cuento_service.routes.cuento import router as cuento_router
from preguntas_service.routes.pregunta import router as pregunta_router
from respuesta_service.routes.respuesta import router as respuesta_router
from auth_service.routes.login import router as auth_router

from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gateway Local")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# MONTA AMBOS SERVICIOS EN EL MISMO SERVIDOR
app.include_router(cuento_router, prefix="/cuento_service")
app.include_router(pregunta_router, prefix="/preguntas_service")
app.include_router(respuesta_router, prefix="/responder_service")
app.include_router(auth_router, prefix="/auth_service")