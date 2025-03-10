from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *


class AutoresView(Frame):    
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None
        self.frame_tabla = None

    def ocultar(self):
        self.pack_forget()
    
    def set_controller(self, controller):
        """Asigna el controlador a la vista."""
        self.controller = controller

    def update_list(self, autores):
        self.frame_tabla = Frame(self)
        self.frame_tabla.pack(fill="x", expand=True, padx=10, pady=10)
        self.tabla = Treeview(self.frame_tabla, columns=("id", "nombre", "apellidos", "nacionalidad", "fecha_nacimiento"), show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.column("id", width=5)
        self.tabla.column("nombre", width=15)
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.column("apellidos", width=20)
        self.tabla.heading("apellidos", text="Apellidos")
        self.tabla.column("nacionalidad", width=10)
        self.tabla.heading("nacionalidad", text="Nacionalidad")
        self.tabla.column("fecha_nacimiento", width=20)
        self.tabla.heading("fecha_nacimiento", text="Fecha de Nacimiento")
        self.tabla.pack(fill="x", padx=10, pady=10)

        self.pack(fill="x", expand=True)
        
        # Botones (descomentados y corregidos)
        Button(self.frame_tabla, text="Crear Autor", command=self._crear).pack(side="left", padx=5)
        Button(self.frame_tabla, text="Modificar Autor", command=self._edit_product).pack(side="left", padx=5)
        Button(self.frame_tabla, text="Eliminar Autor", command=self._delete_product).pack(side="left", padx=5)
        
        for autor in autores:
            self.tabla.insert("", "end", values=(
                autor["id"],
                autor["nombre"],
                autor["apellidos"],
                autor["nacionalidad"],
                autor["fecha_nacimiento"]
            ))
    
    def _crear(self):
        self.controller.crear_autor()

    def _edit_product(self):
        selected = self.tabla.selection()
        if selected:
            item = self.tabla.item(selected[0])
            autor_id = item['values'][0] 
            if self.controller:
                self.controller.show_form_view(autor_id) 
        else:
            messagebox.showwarning("Advertencia", "Seleccione un registro")

    def _delete_product(self):
        """Maneja la eliminación de un libro."""
        selected = self.tabla.selection()
        if selected:
            item_id = self.tabla.item(selected[0])['values'][0]
            if self.controller:
                self.controller.eliminar_autor(item_id)
        else:
            messagebox.showwarning("Advertencia", "Seleccione un registro")

