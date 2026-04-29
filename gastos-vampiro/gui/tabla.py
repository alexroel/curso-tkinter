from tkinter import ttk, messagebox

from logic.gestor_gastos import guardar_suscripciones

class Tabla(ttk.Frame):
    def __init__(self, master, suscripciones):
        super().__init__(master, style="Main.TFrame")
        self.pack(fill="both", expand=True)

        self.suscripciones = suscripciones

        self._crear_resumen()
        self._crear_tabla()
        self._crear_footer()


    def _crear_resumen(self):
        frame = ttk.Frame(self, style="Main.TFrame")
        frame.pack(fill="x", pady=16, padx=16)

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
        frame = ttk.Frame(self)
        frame.pack(fill="both", expand=True, padx=16, pady=(8, 5))

        columnas = ("num", "nombre", "costo", "fecha")

        self.tree = ttk.Treeview(
            frame, 
            columns=columnas,
            show="headings", selectmode="browse", height=5,
        )
        self.tree.pack(side="left", fill="both", expand=True)

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
        scrollbar.pack(side="right", fill="y")

        # Label para cuando no hay datos
        self.lbl_vacio = ttk.Label(
            frame,
            text="No hay suscripciones registradas\nAgrega una para comenzar",
            justify="center",
        )

    def _crear_footer(self):
        frame = ttk.Frame(self, style="Main.TFrame")
        frame.pack(fill="x", padx=16, pady=(0, 12))

        ttk.Button(
            frame,
            text="🗑  Eliminar Seleccionada",
            cursor="hand2",
            command=self._eliminar_suscripcion,
            style="Danger.TButton",
        ).pack(side="left", pady=10)

        self.lbl_anual = ttk.Label(
            frame, text="",
            style="Anual.TLabel",
        )
        self.lbl_anual.pack(side="left", expand=True)


    def _actualizar_tabla(self):
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
            self.lbl_anual.configure(
                text=f"Gasto anual estimado: S/. {total * 12:,.2f}",
            )
        else:
            self.lbl_anual.configure(text="")

        # Actualizar título de la ventana principal
        self.winfo_toplevel().title(f"Gastos Vampiro — S/. {total:,.2f}/mes")

    def _eliminar_suscripcion(self):
        seleccion = self.tree.selection()
        if not seleccion:
            messagebox.showinfo(
                "Sin Selección",
                "Selecciona una suscripción de la tabla para eliminarla.",
            )
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
                self._actualizar_tabla()

            


        

        