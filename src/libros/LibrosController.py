from .Libro import Libro
from .LibrosView import LibrosView
from .FormView import FormView
from tkinter import messagebox


class LibrosController:
    def __init__(self, base_view):
        self.base_view = base_view
        self.model = Libro()
        # Inicializa las vistas y asigna el controlador
        self.libros_view = LibrosView(self.base_view)
        self.form_view = FormView(self.base_view)
        self.libros_view.set_controller(self)
        self.form_view.set_controller(self)
        self.show_list_view()

    def show_list_view(self):
        self.base_view.switch_frame(LibrosView)
        self.base_view.current_frame.set_controller(self)  # Actualiza el controlador
        self.refresh_data()

    def refresh_data(self):
        libros = self.model.listar_todos()
        if libros is not None:
            self.libros_view.update_list(libros)  # Ahora existe el atributo
        else:
            self.show_error("Error al cargar datos")

    def show_form_view(self, libro_id):
        try:
            self.base_view.switch_frame(FormView)
            if libro_id:
                libro = self.model.mostrar_libro(libro_id)
                if libro:
                    self.base_view.switch_frame(FormView)
                    self.form_view.load_data(libro)
        except Exception as e:
            print(f"Error al mostrar el formulario: {e}")
            self.show_error("Error de conexión con la base de datos")
    
        

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
        self.model.eliminar_registro(id)
        self.show_list_view()
    
    
    def show_error(self, message):
        """Muestra un mensaje de error."""
        messagebox.showerror("Error", message)
