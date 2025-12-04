from sqlalchemy import Column, Integer
from database import Base

class Control(Base):
    __tablename__ = "control"

    id_control = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, nullable=False)
    id_cuento = Column(Integer, nullable=False)
    estrella =  Column(Integer, nullable=False)