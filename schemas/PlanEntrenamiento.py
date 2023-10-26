from pydantic import BaseModel

class PlanEntrenamiento(BaseModel):
    
    cliente_id: int
    detalles: str
    descargas_restantentes: int
    