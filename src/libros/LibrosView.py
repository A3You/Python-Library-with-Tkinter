from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

class LibrosView(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = None  # Inicializa el controlador como None
        self._create_widgets()
    
    def set_controller(self, controller):
        """Asigna el controlador a la vista."""
        self.controller = controller

    def _create_widgets(self):
        # Tabla
        self.tabla = Treeview(self, columns=("id", "titulo", "precio", "editorial", "autores"), show="headings")
        self.tabla.heading("id", text="ID")
        self.tabla.heading("titulo", text="Título")
        self.tabla.heading("precio", text="Precio")
        self.tabla.heading("editorial", text="Editorial")
        self.tabla.heading("autores", text="Autores")
        self.tabla.pack(fill="x", expand=True, padx=10, pady=10)
        # self._mostrar_libros([])  # Muestra una lista vacía inicialmente

        # Controles
        btn_frame = Frame(self)
        btn_frame.pack(padx=10, pady=5)

        # Botones (descomentados y corregidos)
        Button(btn_frame, text="Crear Libro", command=self._new_product).pack(side="left", padx=5)
        Button(btn_frame, text="Modificar Libro", command=self._edit_product).pack(side="left", padx=5)
        Button(btn_frame, text="Eliminar Libro", command=self._delete_product).pack(side="left", padx=5)

    def _mostrar_libros(self, libros):
        """
        Muestra los datos de los libros en la tabla.
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

    def _new_product(self):
        """Maneja la creación de un nuevo libro."""
        if self.controller:
            self.controller.show_form_view()

    def _edit_product(self):
        """Maneja la edición de un libro existente."""
        selected = self.tabla.selection()
        if selected:
            item_id = self.tabla.item(selected[0])['values'][0]
            if self.controller:
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

    def update_list(self, libros):
        """Actualiza la lista de libros en la tabla."""
        self._mostrar_libros(libros)