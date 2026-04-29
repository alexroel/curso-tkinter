import tkinter as tk

from gui.app import GastosVampiroApp


def main():
    ventana = tk.Tk()
    app = GastosVampiroApp(ventana)
    ventana.mainloop()

if __name__ == "__main__":
    main()