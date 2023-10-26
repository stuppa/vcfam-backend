from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    id_google: str  
    numero: str
    peso_actual: float
    imc_actual: float
    estatura: float
    edad: int
    objetivo: str
    historia: str
    alergias: str
    enfermedad: str
    tiempo_eje: str
    tiempo_disp_eje: str
    com_live_style: str
    live_style: str
    lesion: str
    com_alergia: str
    com_fav: str
    com_nofav: str
    pago: str
    