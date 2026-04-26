"""
🧛 Gastos Vampiro - Rastreador de Suscripciones
Punto de entrada de la aplicación.

Ejecutar con:  python main.py
"""

import sys
import os
import tkinter as tk

# Agregar el directorio raíz del proyecto al path para que los imports funcionen
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from gui.app import GastosVampiroApp

def main():
    root = tk.Tk()
    app = GastosVampiroApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
