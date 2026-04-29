from tkinter import ttk, messagebox

class Formulario(ttk.LabelFrame):
    def __init__(self, master, suscripciones, refrescar_tabla):
        super().__init__(
            master,
            text="➕ Agregar Nueva Suscripción",
            padding=(20, 14),
            style="Card.TLabelframe",
        )

        self.suscripciones = suscripciones
        self.refrescar_tabla = refrescar_tabla


        self.pack(fill="x", padx=16, pady=(16, 0))

        # ── Fila 0: Labels ─────────────────────
        ttk.Label(
            self,
            text = "Nombre: ",
            style="Card.TLabel",
        ).grid(row=0, column=0, sticky="w", padx=8, pady=(8, 0))

        ttk.Label(
            self,
            text = "Costo (S/.): ",
            style="Card.TLabel",
        ).grid(row=0, column=2, sticky="w", padx=8, pady=(8,0))

        # ── Fila 1: Entradas + Botón ────────────────────────────────────
        self.entry_nombre = ttk.Entry(
            self,
            width=30,
            font=("Segoe UI", 12),
            style="Card.TEntry",
        )
        self.entry_nombre.grid(row=1, column=0, sticky="ew", columnspan=2, padx=8, pady=8)

        self.entry_costo = ttk.Entry(
            self,
            width=14,
            font=("Segoe UI", 12),
            style="Card.TEntry",
        )
        self.entry_costo.grid(row=1, column=2, sticky="ew", padx=8, pady=8)


        ttk.Button(
            self,
            text="Agregar",
            cursor="hand2",
            command=self._agregar_suscripcion,
            style="Accent.TButton",
        ).grid(row=1, column=3, sticky="e", padx=8, pady=8)

        self.entry_nombre.bind("<Return>", lambda e: self.entry_costo.focus_set())
        self.entry_costo.bind("<Return>", lambda e: self._agregar_suscripcion())
        

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
        
        from datetime import datetime
        from logic.gestor_gastos import guardar_suscripciones

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
            
        self.entry_nombre.delete(0, "end")
        self.entry_costo.delete(0, "end")
        self.entry_nombre.focus_set()
        self.refrescar_tabla()







    


