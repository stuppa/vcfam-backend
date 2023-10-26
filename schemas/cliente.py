from pydantic import BaseModel

class Cliente(BaseModel):
    nombre: str
    email: str
    peso_actual: str
    imc_actual: str
    objetivo: str
    historia: str
    alergias: str
    incapacidades: str
    tiempo_ejercicio: str
    comida_fav: str
    comida_nofav: str