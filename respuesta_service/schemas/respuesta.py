from pydantic import BaseModel
from typing import Any, Dict


class ResponderRequest(BaseModel):
	id_usuario: int
	id_cuento: int
	# Comma-separated string: "si,no,si,no" or a list could be accepted by the client
	array_respuestas: str


class ResponderData(BaseModel):
	total: int
	correct: int
	estrella: int
	detalle: Dict[int, bool]


class ResponderResponse(BaseModel):
	message: str
	status: int
	data: ResponderData

class RespuestasResponse(BaseModel):
	message: str
	status: int
	data: list[Any]

