"""
🧛 Gastos Vampiro — Aplicación completa (GUI + lógica de presentación)
Todo el interfaz vive en este archivo usando widgets nativos de tkinter.
"""

import os
from tkinter import ttk, messagebox

from assets.estilos import (
    BG_MAIN, aplicar_estilos,
)
from logic.gestor_gastos import cargar_suscripciones, guardar_suscripciones

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
        self._crear_header()

        from gui.formulario import Formulario
        self.formulario = Formulario(self.root, self.suscripciones, self._refrescar_tabla)

        self._crear_resumen()
        self._crear_tabla()
        self._crear_footer()

        # Cargar datos iniciales
        self._refrescar_tabla()

    # ══════════════════════════════════════════════════════════════════════
    # SECCIONES DE LA INTERFAZ
    # ══════════════════════════════════════════════════════════════════════

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

    def _crear_resumen(self):
        frame = ttk.Frame(self.root, 
                          style="Main.TFrame"
                          )
        frame.pack(fill="x", padx=16, pady=(10, 0))

        ttk.Label(
            frame,
            text="📋 Tus Suscripciones",
            style="MainBold.TLabel",
        ).pack(side="left")

        self.lbl_total = ttk.Label(
            frame,
            text="Total mensual: S/. 0.00",
            style="TotalLabel.TLabel",
        )
        self.lbl_total.pack(side="right")

    def _crear_tabla(self):
        frame = ttk.Frame(self.root, 
                          style="Main.TFrame"
                          )
        frame.pack(fill="both", expand=True, padx=16, pady=(8, 5))

        columnas = ("num", "nombre", "costo", "fecha")
        self.tree = ttk.Treeview(frame, columns=columnas, show="headings", selectmode="browse", height=5)

        self.tree.heading("num", text="#")
        self.tree.heading("nombre", text="Suscripción")
        self.tree.heading("costo", text="Costo Mensual")
        self.tree.heading("fecha", text="Fecha Agregada")

        self.tree.column("num", width=40, anchor="center", minwidth=30)
        self.tree.column("nombre", width=200, anchor="w", minwidth=100)
        self.tree.column("costo", width=120, anchor="center", minwidth=80)
        self.tree.column("fecha", width=120, anchor="center", minwidth=80)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)

        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # Label para cuando no hay datos
        self.lbl_vacio = ttk.Label(
            frame,
            text="No hay suscripciones registradas\nAgrega una para comenzar",
            style="Main.TLabel",
            justify="center",
        )

    def _crear_footer(self):
        frame = ttk.Frame(self.root, style="Main.TFrame")
        frame.pack(fill="x", padx=16, pady=(0, 12))

        ttk.Button(
            frame,
            text="🗑  Eliminar Seleccionada",
            style="Danger.TButton",
            command=self._eliminar_suscripcion,
            cursor="hand2",
        ).pack(side="left")

        self.lbl_anual = ttk.Label(frame, text="", 
                                   style="Anual.TLabel"
                                   )
        self.lbl_anual.pack(side="left", expand=True)

        from logic.exportar_pdf import exportar_pdf

        ttk.Button(
            frame,
            text="📄  Exportar PDF",
            style="Secondary.TButton",
            command=lambda: exportar_pdf(self.suscripciones),
            cursor="hand2",
        ).pack(side="right")

    # ══════════════════════════════════════════════════════════════════════
    # LÓGICA DE NEGOCIO
    # ══════════════════════════════════════════════════════════════════════
    def _eliminar_suscripcion(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo("Sin Selección", "Selecciona una suscripción de la tabla para eliminarla.")
            return

        valores = self.tree.item(seleccion[0])["values"]
        nombre = valores[1]

        confirmar = messagebox.askyesno(
            "Confirmar Eliminación",
            f'¿Eliminar la suscripción "{nombre}"?',
        )

        if confirmar:
            idx = int(valores[0]) - 1
            if 0 <= idx < len(self.suscripciones):
                self.suscripciones.pop(idx)
                try:
                    guardar_suscripciones(self.suscripciones)
                except IOError as e:
                    messagebox.showerror("Error", f"No se pudo guardar:\n{e}")
                self._refrescar_tabla()

    def _refrescar_tabla(self):
        # Limpiar tabla
        for item in self.tree.get_children():
            self.tree.delete(item)

        total = 0.0
        if self.suscripciones:
            self.lbl_vacio.place_forget()
            for i, sub in enumerate(self.suscripciones):
                costo = sub.get("costo", 0)
                total += costo
                self.tree.insert(
                    "", "end",
                    values=(i + 1, 
                    sub.get("nombre", ""), 
                    f"S/. {costo:,.2f}", 
                    sub.get("fecha", "")),
                )
        else:
            self.lbl_vacio.place(relx=0.5, rely=0.5, anchor="center")

        self.lbl_total.configure(text=f"Total mensual: S/. {total:,.2f}")

        if total > 0:
            self.lbl_anual.configure(text=f"Gasto anual estimado: S/. {total * 12:,.2f}")
        else:
            self.lbl_anual.configure(text="")

        self.root.title(f"Gastos Vampiro — S/. {total:,.2f}/mes")
