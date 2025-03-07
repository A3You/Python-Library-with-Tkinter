from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


class LibrosView(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.frame_tabla = None
    
    def ocultar(self):
        self.pack_forget()
    
    def set_controller(self, controller):
        """Asigna el controlador a la vista."""
        self.controller = controller

    def update_list(self, libros):

        self.frame_tabla = Frame(self)
        self.frame_tabla.pack(fill="x", expand=True, padx=10, pady=10)
        self.tabla = Treeview(self.frame_tabla, columns=("id", "titulo", "precio", "editorial", "autores"), show="headings")
        self.tabla.column("id", width=5)
        self.tabla.heading("id", text="ID")
        self.tabla.heading("titulo", text="Título")
        self.tabla.column("precio", width=10)
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("editorial", text="Editorial")
        self.tabla.heading("autores", text="Autores")
        self.tabla.pack(fill="x", expand=True, padx=10, pady=10)

        self.pack(fill="x", expand=True)
        
        # Botones (descomentados y corregidos)
        Button(self.frame_tabla, text="Crear Libro", command=self._crear).pack(side="left", padx=5)
        Button(self.frame_tabla, text="Modificar Libro", command=self._edit_product).pack(side="left", padx=5)
        Button(self.frame_tabla, text="Eliminar Libro", command=self._delete_product).pack(side="left", padx=5)
        
        for libro in libros:
            self.tabla.insert("", "end", values=(
                libro["id"],
                libro["titulo"],
                libro["precio"],
                libro["editorial"],
                libro["autores"]
            ))
    
    def _crear(self):
        self.controller.crear_libro()

    def _edit_product(self):
        """Maneja la edición de un libro existente."""
        selected = self.tabla.selection()
        if selected:
            item_id = self.tabla.item(selected[0])
            if self.controller:
                self.pack_forget()
                self.controller.show_form_view(item_id)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un registro")

    def _delete_product(self):
        """Maneja la eliminación de un libro."""
        selected = self.tabla.selection()
        if selected:
            item_id = self.tabla.item(selected[0])['values'][0]
            if self.controller:
                self.controller.eliminar_libro(item_id)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un registro")

