from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox

from app.libros.LibrosController import LibrosController
from app.autores.AutoresController import AutoresController
# from app.editoriales.EditorialesController import EditorialesController

class BaseView(Tk):
    def __init__(self):
        super().__init__()
        self.title("Libros")
        self.geometry("800x400")
        self.libros_controller = None
        self.autores_controller = None
        # self.editoriales_controller = None
        menubar = Menu(self)
        self.config(menu=menubar)

        
        self.welcome_label = Label(self, text="Bienvenido a la aplicación de gestión de libros", font=("Century Gothic", 32), wraplength=500, justify=CENTER)
        self.welcome_label.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Menu options
        menubar.add_command(label="Libros", command=self._set_libros_controller)
        menubar.add_command(label="Autores", command=self._set_autores_controller)
        # menubar.add_command(label="Editoriales", command=self._set_editoriales_controller)
        menubar.add_command(label="Editoriales", command=lambda: messagebox.showinfo("Editoriales", "Pendiente de implementar"))

    def _confirm_exit(self):
        if messagebox.askokcancel("Salir", "¿Desea salir?"):
            self.destroy()

    def _set_autores_controller(self):
        if self.welcome_label:
            self.welcome_label.pack_forget()
        if self.libros_controller:
            self.libros_controller.ocultar()
        if self.autores_controller:
            self.autores_controller.ocultar()
        # if self.editoriales_controller:
        #     self.editoriales_controller.pack_forget()
        self.autores_controller = AutoresController(self)

    def _set_libros_controller(self):
        if self.welcome_label:
            self.welcome_label.pack_forget()
        if self.libros_controller:
            self.libros_controller.ocultar()
        if self.autores_controller:
            self.autores_controller.ocultar()
        self.libros_controller = LibrosController(self)
    
    # def _set_editoriales_controller(self):
    #     self.editoriales_controller = EditorialesController(self)

