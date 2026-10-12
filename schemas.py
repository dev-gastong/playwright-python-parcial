# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field

class Evento(BaseModel):
    nombre: str = Field(min_length=3, max_length=50)
    fecha: str = Field(pattern=r"\d{4}-\d{2}-\d{2}")
    lugar: str
    descripcion: str | None = None
    



