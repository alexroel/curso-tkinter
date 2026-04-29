from tkinter import filedialog, messagebox
from datetime import datetime

def exportar_pdf(suscripciones: list[dict]):
    if not suscripciones:
        messagebox.showinfo("Sin Datos", "No hay suscripciones para exportar.")
        return
    
    ruta = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile=f"gastos_vampiro_{datetime.now().strftime('%Y%m%d')}.pdf",
        title="Guardar Reporte PDF",
    )

    if not ruta:
        return
    
    try:
        from fpdf import FPDF

        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)

        pdf.set_font("Helvetica", "B", 24)
        pdf.cell(0, 16, "Gastos Vampiro", new_x="LMARGIN", new_y="NEXT", align="C")

        pdf.set_font("Helvetica", "", 11)
        pdf.cell(
            0, 8,
            f"Reporte generado el {datetime.now().strftime('%d/%m/%Y a las %H:%M')}",
            new_x="LMARGIN", new_y="NEXT", align="C",
        )

        pdf.ln(10)

        total = 0
        for s in suscripciones:
            total += s.get("costo", 0)

        pdf.set_font("Helvetica", "B", 14)
        pdf.cell(
            0, 12,
            f"  Total mensual: S/. {total:,.2f}   |   Total anual: S/. {total * 12:,.2f}  ",
            new_x="LMARGIN", new_y="NEXT", align="C",
        )
        pdf.ln(8)

        pdf.set_font("Helvetica", "B", 11)
        col_widths = [15, 75, 50, 50]

        headers = ["#", "Suscripcion", "Costo Mensual", "Fecha"]

        for w, h in zip(col_widths, headers):
            pdf.cell(w, 10, h, border=1, align="C")
        pdf.ln()

        pdf.set_font("Helvetica", "", 10)
        for i, sub in enumerate(suscripciones):
            pdf.cell(col_widths[0], 9, str(i + 1), border=1, align="C")
            pdf.cell(col_widths[1], 9, sub.get("nombre", ""), border=1, align="L")
            pdf.cell(col_widths[2], 9, f"S/. {sub.get('costo', 0):,.2f}", border=1, align="C")
            pdf.cell(col_widths[3], 9, sub.get("fecha", ""), border=1, align="C")
            pdf.ln()

        pdf.output(ruta)
        messagebox.showinfo("PDF Exportado", f"Reporte guardado en:\n{ruta}")




        


    except ImportError:
        messagebox.showerror(
            "Dependencia Faltante",
            "Necesitas instalar fpdf2:\n\npip install fpdf2",
        )
    except Exception as e:
        messagebox.showerror("Error al Exportar", f"No se pudo generar el PDF:\n{e}")