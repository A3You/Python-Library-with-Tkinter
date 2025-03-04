import tkinter as tk
from models.Libro import Libro
from views.libros.LibrosView import LibrosView
from controllers.LibrosController import LibrosController


class Libros(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Libros")
        self.geometry("800x400")
    
        self.view = LibrosView(self)
        self.controller = LibrosController(self.view, Libro())

        self.controller.listar_libros()


if __name__ == "__main__":
    libros = Libros()
    libros.mainloop()
