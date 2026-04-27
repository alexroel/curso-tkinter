"""
🧛 Gastos Vampiro — Aplicación completa (GUI + lógica de presentación)
Todo el interfaz vive en este archivo usando widgets nativos de tkinter.
"""

import os
import tkinter as tk
from tkinter import ttk, messagebox

from assets.estilos import (
    BG_MAIN, aplicar_estilos,
)
from logic.gestor_gastos import cargar_suscripciones

# Ruta al directorio de assets (relativa a este archivo)
_ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets")


class GastosVampiroApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gastos Vampiro")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        self.root.iconbitmap(os.path.join(_ASSETS_DIR, "vampire.ico"))
        self.root.configure(bg=BG_MAIN)

        # ── Aplicar estilos ttk ─────────────────────────────────────────
        self.style = ttk.Style(self.root)
        aplicar_estilos(self.style)

        # Datos
        self.suscripciones = cargar_suscripciones()

        # ── Construir UI ─────────────────────────────────────────────────
        self._crear_menu()
        self._crear_header()

        from gui.formulario import Formulario
        from gui.tabla import Tabla

        self.formulario = Formulario(
            self.root, self.suscripciones,
            lambda: self.tabla.refrescar(),
        )
        self.tabla = Tabla(self.root, self.suscripciones)

        # Cargar datos iniciales
        self.tabla.refrescar()

    # ══════════════════════════════════════════════════════════════════════
    # SECCIONES DE LA INTERFAZ
    # ══════════════════════════════════════════════════════════════════════

    def _crear_menu(self):
        """Crea la barra de menú principal de la aplicación."""
        barra_menu = tk.Menu(self.root)
        self.root.config(menu=barra_menu)

        # ── Menú Archivo ─────────────────────────────────────────────────
        menu_archivo = tk.Menu(barra_menu, tearoff=0)
        menu_archivo.add_command(
            label="📄 Exportar PDF",
            command=self._exportar_pdf,
            accelerator="Ctrl+E",
        )
        menu_archivo.add_separator()
        menu_archivo.add_command(
            label="🚪 Salir",
            command=self._salir,
            accelerator="Ctrl+Q",
        )
        barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

        # ── Acerca de (directo en la barra) ──────────────────────────────
        barra_menu.add_command(
            label="Acerca de",
            command=self._mostrar_acerca_de,
        )

        # ── Atajos de teclado ────────────────────────────────────────────
        self.root.bind("<Control-e>", lambda e: self._exportar_pdf())
        self.root.bind("<Control-q>", lambda e: self._salir())

    def _crear_header(self):
        # Frame con fondo ACCENT púrpura
        frame = ttk.Frame(self.root, 
                          style="Header.TFrame"
                          )
        frame.pack(fill="x")

        # Contenedor interno para padding
        inner = ttk.Frame(frame, 
                          style="Header.TFrame"
                          )
        inner.pack(fill="x", padx=24, pady=(28, 24))

        # Título
        ttk.Label(
            inner,
            text="🧛 Gastos Vampiro",
            style="HeaderTitle.TLabel"
        ).pack()

        # Subtítulo
        ttk.Label(
            inner,
            text="Rastreador de suscripciones que chupan tu dinero 💸",
            style="HeaderSubTitle.TLabel"
        ).pack(pady=(2, 0))

    # ══════════════════════════════════════════════════════════════════════
    # ACCIONES DEL MENÚ
    # ══════════════════════════════════════════════════════════════════════

    def _exportar_pdf(self):
        """Exporta las suscripciones a un archivo PDF."""
        from logic.exportar_pdf import exportar_pdf
        exportar_pdf(self.suscripciones)

    def _salir(self):
        """Cierra la aplicación con confirmación."""
        if messagebox.askokcancel("Salir", "¿Estás seguro de que deseas salir?"):
            self.root.destroy()

    def _mostrar_acerca_de(self):
        """Muestra información sobre la aplicación."""
        messagebox.showinfo(
            "Acerca de Gastos Vampiro",
            "🧛 Gastos Vampiro v1.0\n\n"
            "Rastreador de suscripciones que\n"
            "chupan tu dinero 💸\n\n"
            "Desarrollado con Python y Tkinter",
        )
