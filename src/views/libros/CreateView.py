from tkinter import *
from tkinter.ttk import *
from .styles import styles


class CreateView(Frame):
    # styles()
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Label
        self.label = Label(self, text="Insertar Libro Nuevo", font=("Poppins", 18))
        self.label.pack(pady=20)

        # Formulario
        self.tabla = Treeview(self, columns=("id", "titulo", "precio", "editorial", "autores"), show="headings")
        self.tabla.column("id", width=50, anchor="center")
        self.tabla.column("titulo", width=250, anchor="center")
        self.tabla.column("precio", width=100, anchor="center")
        self.tabla.column("editorial", width=150, anchor="center")
        self.tabla.column("autores", width=200, anchor="center")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("titulo", text="Título")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("editorial", text="Editorial")
        self.tabla.heading("autores", text="Autores")
        self.tabla.pack(fill="x", expand=True)

    def mostrar_libros(self, libros):
        """
        Muestra los datos de los libros en la tabla
        """
        self.tabla.delete(*self.tabla.get_children())
        for libro in libros:
            self.tabla.insert(
                "",
                "end",
                values=(
                    libro["id"],
                    libro["titulo"],
                    libro["precio"],
                    libro["editorial"],
                    libro["autores"],
                ),
            )
        self.pack(fill="x", expand=True)

