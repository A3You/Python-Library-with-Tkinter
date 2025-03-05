from tkinter import *
from tkinter.ttk import *

class BaseView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Libros")
        self.geometry("800x400")
        self.current_frame = None  # Frame actualmente visible
        self.controller = None  # Controlador asociado a la vista
    
    def switch_frame(self, frame_class):
        # Destruye el frame actual si existe
        if self.current_frame:
            self.current_frame.destroy()
        
        # Crea el nuevo frame
        new_frame = frame_class(self)
        self.current_frame = new_frame
    
    def set_controller(self, controller):
        """
        Asigna un controlador a la vista.
        
        Args:
            controller: El controlador que manejará la lógica de la vista.
        """
        self.controller = controller