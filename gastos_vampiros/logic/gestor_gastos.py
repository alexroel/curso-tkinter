"""
🧛 Gastos Vampiro — Gestor de Gastos (Capa de Lógica de Negocio)
Funciones para leer, escribir y procesar los datos de suscripciones en JSON.
"""

import json
import os

# Nombre del archivo de datos (relativo a data/)
DATA_FILENAME = "gastos.json"


def _ruta_datos():
    """Devuelve la ruta absoluta al archivo de datos JSON."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, "data", DATA_FILENAME)


def cargar_suscripciones()-> list[dict]:
    """Carga las suscripciones desde el archivo JSON.

    Returns:
        list[dict]: Lista de diccionarios con las suscripciones.
                    Cada diccionario contiene: nombre, costo, fecha.
    """
    ruta = _ruta_datos()
    if os.path.exists(ruta):
        try:
            with open(ruta, "r", encoding="utf-8") as f:
                datos = json.load(f)
                if isinstance(datos, list):
                    return datos
        except (json.JSONDecodeError, IOError):
            pass
    return []


def guardar_suscripciones(suscripciones: list[dict])-> None:
    """Guarda las suscripciones en el archivo JSON.

    Args:
        suscripciones (list[dict]): Lista de suscripciones a guardar.

    Raises:
        IOError: Si no se puede escribir el archivo.
    """
    ruta = _ruta_datos()

    # Crear directorio data/ si no existe
    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    with open(ruta, "w", encoding="utf-8") as f:
        json.dump(suscripciones, f, ensure_ascii=False, indent=2)
