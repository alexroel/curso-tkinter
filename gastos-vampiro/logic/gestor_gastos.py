import json
from pathlib import Path
import sys

# Ruta absoluta al archivo de datos JSON
def obtener_ruta_base():
    """Retorna la ruta base, ya sea en desarrollo o compilado como .exe"""
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS)
    
    return Path(__file__).resolve().parent.parent

RUTA_DATOS = obtener_ruta_base() / "data" / "gastos.json"

# Cargar suscripciones 
def cargar_suscripciones() -> list[dict]:
    """Carga las suscripciones desde el archivo JSON.

    Returns:
        list[dict]: Lista de diccionarios con las suscripciones.
                    Cada diccionario contiene: nombre, costo, fecha.
    """
    ruta = RUTA_DATOS
    if ruta.exists():
        with open(ruta, "r", encoding="utf-8") as archivo:
            data = json.load(archivo)
            if isinstance(data, list):
                return data
            
    return []

# Guardar suscripciones
def guardar_suscripciones(suscripciones: list[dict]):
    """Guarda las suscripciones en el archivo JSON.

    Args:
        suscripciones (list[dict]): Lista de suscripciones a guardar.
    """
    ruta = RUTA_DATOS

    ruta.parent.mkdir(parents=True, exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(suscripciones, archivo, indent=2, ensure_ascii=False)



