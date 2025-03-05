from .Libro import Libro
from .LibrosView import LibrosView
from .FormView import FormView
from tkinter import messagebox


class LibrosController:
    def __init__(self, base_view):
        self.base_view = base_view
        self.model = Libro()  # Inicializa el modelo

        # Inicializa las vistas
        self.libros_view = LibrosView(self.base_view)
        self.form_view = FormView(self.base_view)

        # Asigna el controlador a las vistas
        self.libros_view.set_controller(self)
        self.form_view.set_controller(self)

        # Muestra la vista inicial
        self.show_list_view()
    
    def listar_libros(self):
        """Muestra la vista de lista de libros."""
        self.base_view.switch_frame(LibrosView)
        self.refresh_data()
    
    def refresh_data(self):
        """Actualiza la lista de libros en la vista."""
        libros = self.model.listar_todos()
        if libros:
            self.libros_view.update_list(libros)
        else:
            print("No se encontraron libros en la base de datos.")  # Depuración
        
    def crear_libro(self):
        """Prepara el formulario para crear un nuevo libro."""
        self.form_view.current_id = None
        self.base_view.switch_frame(FormView)
    
    def guardar_libro(self, titulo, precio, editorial, fecha_publicacion, autores):
        """Guarda un libro (crear o modificar)."""
        if self.form_view.current_id:
            # Modificar libro existente
            self.model.modificar_registro(self.form_view.current_id, {
                "titulo": titulo,
                "precio": precio,
                "id_editorial": editorial,
                "autores": autores
            })
        else:
            # Crear nuevo libro
            self.model.crear_libro(titulo, precio, editorial, fecha_publicacion, autores)
        
        # Vuelve a la vista de lista
        self.show_list_view()
    
    def eliminar_libro(self, id):
        """Elimina un libro por su ID."""
        self.model.eliminar_registro(id)
        self.refresh_data()
    
    def show_form_view(self, libro_id=None):
        """Muestra el formulario para editar un libro existente."""
        self.base_view.switch_frame(FormView)
        if libro_id:
            libro = self.model.buscar_por_id(libro_id)
            if libro:
                self.form_view.load_data(libro)
    
    def show_list_view(self):
        """Muestra la vista de lista de libros."""
        self.base_view.switch_frame(LibrosView)
        self.refresh_data()
    
    def show_error(self, message):
        """Muestra un mensaje de error."""
        messagebox.showerror("Error", message)