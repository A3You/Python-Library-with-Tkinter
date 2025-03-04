from tkinter import *
from tkinter.ttk import *
from models.Libro import Libro
from views.libros.LibrosView import LibrosView
from controllers.LibrosController import LibrosController


class Libros(Tk):
    def __init__(self):
        super().__init__()

        self.title("Libros")
        self.geometry("800x400")

        self.frames = {}
        self.create_frames()

        self.show_frame("LibrosView")

    def create_frames(self):
        self.frames["LibrosView"] = LibrosView(self)
        # self.frames["OtraVista"] = Frame(self)  # Ejemplo de otra vista

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.controller = LibrosController(self.frames["LibrosView"], Libro())
        self.controller.listar_libros()

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


if __name__ == "__main__":
    libros = Libros()
    libros.mainloop()
