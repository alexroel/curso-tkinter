import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

from logic.gestor_gastos import guardar_suscripciones


class Formulario(ttk.LabelFrame):
    def __init__(self, master, suscripciones, refrescar_tabla):
        super().__init__(master, 
                         text="  ➕ Agregar Nueva Suscripción  ", 
                         style="Card.TLabelframe", padding=(20, 14)
                         )
        self.pack(fill="x", padx=16, pady=(12, 0))

        self.suscripciones = suscripciones
        self.refrescar_tabla = refrescar_tabla

        # Fondo blanco dentro del LabelFrame
        self.configure(style="Card.TLabelframe")

        # ── Fila 0: Labels ──────────────────────────────────────────────
        ttk.Label(self, 
                  text="Nombre:", 
                  style="Card.TLabel"
                  ).grid(
            row=0, column=0, sticky="w", padx=(0, 8), pady=(0, 4),
        )

        ttk.Label(self, text="Costo (S/.):", 
                  style="Card.TLabel"
                  ).grid(
            row=0, column=2, sticky="w", padx=(12, 8), pady=(0, 4),
        )

        # ── Fila 1: Entradas + Botón ────────────────────────────────────
        self.entry_nombre = ttk.Entry(self, width=30, 
                                    style="Card.TEntry", 
                                    )
        self.entry_nombre.grid(row=1, column=0, columnspan=2, sticky="ew", padx=(0, 8), ipady=3)

        self.entry_costo = ttk.Entry(self, width=14, 
                                    style="Card.TEntry", 
                                    )
        self.entry_costo.grid(row=1, column=2, sticky="ew", padx=(12, 8), ipady=3)

        self.entry_costo.bind("<Return>", lambda e: self._agregar_suscripcion())
        self.entry_nombre.bind("<Return>", lambda e: self.entry_costo.focus_set())

        ttk.Button(
            self,
            text="✚  Agregar",
            style="Accent.TButton",
            command=self._agregar_suscripcion,
            cursor="hand2",
        ).grid(row=1, column=3, sticky="e", padx=(4, 0))

        # ── Configurar pesos de columna ─────────────────────────────────
        self.columnconfigure(0, weight=0)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=0)
        self.columnconfigure(3, weight=0)

    def _agregar_suscripcion(self):
        nombre = self.entry_nombre.get().strip()
        costo_str = self.entry_costo.get().strip()

        if not nombre:
            messagebox.showwarning("Campo Vacío", "Por favor ingresa el nombre de la suscripción.")
            self.entry_nombre.focus_set()
            return

        if not costo_str:
            messagebox.showwarning("Campo Vacío", "Por favor ingresa el costo de la suscripción.")
            self.entry_costo.focus_set()
            return

        try:
            costo = float(costo_str)
            if costo <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Error de Formato",
                f'"{costo_str}" no es un número válido.\n\nEjemplo: 15.99',
            )
            self.entry_costo.delete(0, "end")
            self.entry_costo.focus_set()
            return

        suscripcion = {
            "nombre": nombre,
            "costo": round(costo, 2),
            "fecha": datetime.now().strftime("%d/%m/%Y"),
        }

        self.suscripciones.append(suscripcion)

        try:
            guardar_suscripciones(self.suscripciones)
        except IOError as e:
            messagebox.showerror("Error", f"No se pudo guardar:\n{e}")

        self.refrescar_tabla()
        self.entry_nombre.delete(0, "end")
        self.entry_costo.delete(0, "end")
        self.entry_nombre.focus_set()