from app.models.Libro import Libro
from .LibrosView import LibrosView
from .FormView import FormView
from tkinter import messagebox


class LibrosController:
    def __init__(self, base_view):
        self.base_view = base_view
        self.form_view = None
        self.libros_view = LibrosView(self.base_view)
        self.model = Libro()
        self.show_list_view()

    def ocultar(self):
        self.libros_view.ocultar()

    def show_list_view(self):
        self.libros_view = LibrosView(self.base_view)  # Crear vista solo al necesitarla
        self.libros_view.set_controller(self)
        self.refresh_data()

    def refresh_data(self):
        libros = self.model.listar_todos()
        if libros is not None:
            self.libros_view.update_list(libros)  # Ahora existe el atributo
        else:
            self.show_error("Error al cargar datos")

    def show_form_view(self, libro_id):
        try:
            if libro_id:
                self.form_view = FormView(self.libros_view)
                self.form_view.set_controller(self)
                self.form_view.create_widgets() 
                libro = self.model.mostrar_libro(libro_id['values'][0])
                autores_id = self.model.autores_libro(libro_id['values'][0])
                autores_id = [int(a['id_autor']) for a in autores_id]
                
                if libro:
                    self.form_view.load_data(libro, autores_id)
                
        except Exception as e:
            print(f"Error al mostrar el formulario: {e}")
            self.show_error("Error de conexión con la base de datos")

    def show_form_view(self, libro_id):
        try:
            if libro_id:
                # Crear nueva instancia del formulario
                self.form_view = FormView(self.libros_view)
                self.form_view.set_controller(self)
                self.form_view.create_widgets()  # Generar widgets
                
                # Cargar datos después de crear el formulario
                libro = self.model.mostrar_libro(libro_id['values'][0])
                autores_id = self.model.autores_libro(libro_id['values'][0])
                autores_id = [int(a['id_autor']) for a in autores_id]
                
                if libro:
                    self.form_view.load_data(libro, autores_id)
                    
        except Exception as e:
            print(f"Error al mostrar el formulario: {e}")
            self.show_error("Error de conexión con la base de datos")
        
    def crear_libro(self):
        self.form_view = FormView(self.libros_view)
        self.form_view.set_controller(self)
        self.form_view.create_widgets()
    
    def guardar_libro(self, current_id=None, titulo=None, precio=None, editorial=None, fecha_publicacion=None, autores=None):
        if current_id:  
            self.model.modificar_registro(current_id, {
                "titulo": titulo,
                "precio": precio,
                "id_editorial": editorial,
                "fecha_publicacion": fecha_publicacion,
                "autores": autores
            })
        else:  
            self.model.crear_libro(titulo, precio, editorial, fecha_publicacion, autores)
        
        self.form_view.destroy()
        self.ocultar()
        self.show_list_view()
    
    def obtener_autores(self):
        return self.model.listar_autores()
    
    def obtener_editoriales(self):
        return self.model.listar_editoriales()
    
    def eliminar_libro(self, id):
        self.model.eliminar_registro(id)
        self.ocultar()  
        self.show_list_view()    
    
    def show_error(self, message):
        """Muestra un mensaje de error."""
        messagebox.showerror("Error", message)
