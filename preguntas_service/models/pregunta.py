from sqlalchemy import Column, Integer, String
from database import Base

class Pregunta(Base):
    __tablename__ = "preguntas"

    id_pregunta = Column(Integer, primary_key=True, index=True)
    id_cuento = Column(String, nullable=False)
    contenido = Column(String, nullable=False)
    resp_correcta = Column(String, nullable=True)
