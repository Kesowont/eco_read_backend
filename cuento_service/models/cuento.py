from sqlalchemy import Column, Integer, String
from database import Base

class Cuento(Base):
    __tablename__ = "cuento"

    id_cuento = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    text = Column(String, nullable=False)
    image = Column(String, nullable=True)
