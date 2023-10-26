from pydantic import BaseModel
from datetime import date 
class ObjetivoFitness(BaseModel):
    
    nombre: str
    descripcion: str
    fecha_inicio: date
    fecha_fin: date
     