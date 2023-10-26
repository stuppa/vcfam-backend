from pydantic import BaseModel

class Fotos(BaseModel):
    
    cliente_id: int
    foto: bytearray
    
    