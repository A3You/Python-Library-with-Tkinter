from app.models.Autores import Autores
from .AutoresView import AutoresView
from .FormView import FormView
from tkinter import messagebox


class AutoresController:
    def __init__(self, base_view):
        self.base_view = base_view
        self.form_view = None
        self.autores_view = AutoresView(self.base_view)
        self.model = Autores()
        self.show_list_view()
    
    def ocultar(self):
        self.autores_view.ocultar()

    def show_list_view(self):
        self.autores_view = AutoresView(self.base_view) 
        self.autores_view.set_controller(self)
        self.refresh_data()

    def refresh_data(self):
        autores = self.model.listar_autores()
        if autores is not None:
            self.autores_view.update_list(autores)  # Ahora existe el atributo
        else:
            self.show_error("Error al cargar datos")

    def show_form_view(self, autor_id):
        try:
            if autor_id:
                self.form_view = FormView(self.autores_view)
                self.form_view.set_controller(self)
                self.form_view.create_widgets()
                autor = self.model.mostrar_autor(autor_id)
                if autor:
                    self.form_view.load_data(autor, [])
                    
        except Exception as e:
            print(f"Error al mostrar el formulario: {e}")
            self.show_error("Error de conexión con la base de datos")
        

    def crear_autor(self):
        self.form_view = FormView(self.autores_view)
        self.form_view.set_controller(self)
        self.form_view.create_widgets()
        
    
    def guardar_autor(self, current_id=None, nombre=None, apellidos=None, fecha_nacimiento=None, nacionalidad=None, fecha_fallecimiento=None):
        """Guarda un autor (crear o modificar)."""
        if current_id:
            # Modificar autor existente
            self.model.modificar_registro(current_id, {
                "nombre": nombre,
                "apellidos": apellidos,
                "nacionalidad": nacionalidad,
                "fecha_nacimiento": fecha_nacimiento,
                "fecha_fallecimiento": fecha_fallecimiento,
            })
        else:
            # Crear nuevo autor
            self.model.crear_autor(nombre, apellidos, fecha_nacimiento, nacionalidad, fecha_fallecimiento)
        
        # Vuelve a la vista de lista
        self.ocultar()
        self.show_list_view()
    
    def eliminar_autor(self, id):
        self.model.eliminar_registro(id)
        self.ocultar()
        self.show_list_view()
    
    
    def show_error(self, message):
        """Muestra un mensaje de error."""
        messagebox.showerror("Error", message)

