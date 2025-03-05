from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

class BaseView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Libros")
        self.geometry("800x400")
        # Frame actual
        self.current_frame = None
        # Controlador asociado a la vista
        self.controller = None
        # Menu principal
        menubar = Menu(self)
        self.config(menu=menubar)
    
        # Menu libros
        libros_menu = Menu(menubar, tearoff=0)
        libros_menu.add_command(label="Listar", command=lambda: self.controller.show_list_view())
        libros_menu.add_command(label="Crear", command=lambda: self.controller.crear_libro())
        libros_menu.add_separator()
        libros_menu.add_command(label="Salir", command=lambda: self._confirm_exit())
        menubar.add_cascade(label="Libros", menu=libros_menu)
        
        # Menu autores
        autores_menu = Menu(menubar, tearoff=0)
        autores_menu.add_command(label="Listar")
        autores_menu.add_command(label="Crear")
        menubar.add_cascade(label="Autores", menu=autores_menu)
        
        # Menu editoriales
        editoriales_menu = Menu(menubar, tearoff=0)
        editoriales_menu.add_command(label="Listar")
        editoriales_menu.add_command(label="Crear")
        menubar.add_cascade(label="Editoriales", menu=editoriales_menu)
    
    def switch_frame(self, frame_class):
        if self.current_frame:
            self.current_frame.destroy()  # Destruye el frame actual
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill=BOTH, expand=True)  # Empaqueta el nuevo frame
        
    def _confirm_exit(self):
        if messagebox.askokcancel("Salir", "¿Desea salir?"):
            if self.controller:
                self.controller.confirm_exit()
            else:
                self.destroy()
    def set_controller(self, controller):
        """
        Asigna un controlador a la vista.        
        Args:
            controller: El controlador que manejará la lógica de la vista.
        """
        self.controller = controller