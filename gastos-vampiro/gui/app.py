import tkinter as tk
from tkinter import ttk, messagebox
from logic.gestor_gastos import cargar_suscripciones

# Ruta de asset
from pathlib import Path
import sys
def obtener_ruta_base():
    """Retorna la ruta base, ya sea en desarrollo o compilado como .exe"""
    if getattr(sys, 'frozen', False):
        return Path(sys._MEIPASS)
    
    return Path(__file__).resolve().parent.parent
_ASSETS_DIR = obtener_ruta_base() / "assets"


class GastosVampiroApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        root.title("Gastos Vampiro")
        root.geometry("700x680")
        root.resizable(False, False)
        root.iconbitmap(_ASSETS_DIR / "vampire.ico")


        # ── Aplicar estilos ttk ─────────────────────────────────────────
        self.style = ttk.Style(self.root)

        from assets.estilos import aplicar_estilos
        aplicar_estilos(self.style)

        self.frame = ttk.Frame(self.root, style="Main.TFrame")
        self.frame.pack(fill="x")

        # Datos
        self.suscripciones = cargar_suscripciones()

        self._crear_menu()
        self._crear_header()

        from gui.formulario import Formulario
        from gui.tabla import Tabla

        Formulario(self.frame, self.suscripciones, lambda: self.tabla._actualizar_tabla())

        # Mostrar Tabla de información
        
        self.tabla = Tabla(self.frame, self.suscripciones)
        self.tabla._actualizar_tabla()

    
    def _crear_menu(self):
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        # ── Menú Archivo ─────────────────────────────────────────────────
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        menu_archivo.add_command(
            label="Exportar en PDF",
            accelerator="Ctrl+P",
            command=self._exportar_pdf
        )
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label="Salir",
            accelerator="Ctrl+Q",
            command=self._salir
        )

        barra_menu.add_command(
            label="Acerca de",
            command=self._mostrar_acerca_de
        )

        # ── Atajos de teclado ────────────────────────────────────────────
        self.root.bind("<Control-q>", self._salir)
        self.root.bind("<Control-p>", self._exportar_pdf)

    def _crear_header(self):
        inner = ttk.Frame(self.frame, style="Header.TFrame")
        inner.pack(fill="x", ipadx=24, ipady=20)

        #Título
        ttk.Label(
            inner,
            text="🧛 Gastos Vampiro",
            style="HeaderTitle.TLabel"
        ).pack(pady=(28, 0))

        # Subtítulo
        ttk.Label(
            inner,
            text="Rastreador de suscripciones que chupan tu dinero 💸",
            style="HeaderSubTitle.TLabel"
        ).pack(pady=(2, 0))

    def _exportar_pdf(self, event=None):
        from logic.exportar_pdf import exportar_pdf
        exportar_pdf(self.suscripciones)


    def _salir(self, event=None):
        if messagebox.askokcancel("Salir", "¿Estás seguro de que quieres salir?"):
            self.root.destroy()
    
    def _mostrar_acerca_de(self):
        messagebox.showinfo(
            "Acerca de Gastos Vampiro",
            """
            Acerca de Gastos Vampiro,
            🧛 Gastos Vampiro v1.0\n
            Rastreador de suscripciones que\n
            chupan tu dinero 💸\n
            Desarrollado con Python y Tkinter
            """
        )




