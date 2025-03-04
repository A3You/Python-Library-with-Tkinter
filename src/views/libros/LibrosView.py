import tkinter as tk
from tkinter import ttk
class LibrosView(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
    
        #Label
        self.label = tk.Label(self, text="Libros a la venta")
        self.label.pack()
        #Tabla
        self.tabla = ttk.Treeview(self, columns=("id", "titulo", "precio", "editorial", "autores"), show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("titulo", text="Título")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("editorial", text="Editorial")
        self.tabla.heading("autores", text="Autor")
        self.tabla.pack()
        #Botones
        # self.boton_crear = tk.Button(self, text="Crear libro", command=self.crear_libro)
        # self.boton_crear.pack()
        # self.boton_modificar = tk.Button(self, text="Modificar libro", command=self.modificar_libro)
        # self.boton_modificar.pack()
        # self.boton_eliminar = tk.Button(self, text="Eliminar libro", command=self.eliminar_libro)
        # self.boton_eliminar.pack()

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

