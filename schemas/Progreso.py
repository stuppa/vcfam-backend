from pydantic import BaseModel
from datetime import date 

class Progreso(BaseModel):
    
    cliente_id: int
    fecha: date
    peso: float
    imc: float
    medidas_corporales: str
    imagen_progreso: bytearray