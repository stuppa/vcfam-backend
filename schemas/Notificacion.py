from pydantic import BaseModel

class Notificacion(BaseModel):
    
    cliente_id: int
    mensaje: str
    
    