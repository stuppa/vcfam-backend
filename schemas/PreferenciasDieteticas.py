from pydantic import BaseModel

class PreferenciasDieteticas(BaseModel):
    
    cliente_id: int
    tipo_preferencia: str
    alimentos_permitidos: str
    alimentos_prohibidos: str