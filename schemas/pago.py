from pydantic import BaseModel

class Pago(BaseModel):
    cliente_id: int
    comprobante_pago: str
    estado_verificacion: str
    