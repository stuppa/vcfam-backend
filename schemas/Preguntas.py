from pydantic import BaseModel

class Preguntas(BaseModel):
    
    cliente_id: int
    pregunta: str
    respuesta: str