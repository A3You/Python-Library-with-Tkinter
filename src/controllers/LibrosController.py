import sys
sys.path.append("..")
from models.Libro import Libro
from views.libros.LibrosView import LibrosView


class LibrosController:
    def __init__(self, view: LibrosView, model: Libro):
        self.view = view
        self.model = model

        self.view.controller = self
    
    def listar_libros(self):
        libros = self.model.listar_todos()
        self.view.mostrar_libros(libros)
    
    def crear_libro(self):
        self.view.mostrar_formulario_libro()
    
    def guardar_libro(self, titulo, precio, editorial_id, autor_id):
        self.model.crear_registro({"titulo": titulo, "precio": precio, "editorial_id": editorial_id, "autor_id": autor_id})
        self.listar_libros()
    
    def eliminar_libro(self, id):
        self.model.eliminar_registro(id)
        self.listar_libros()
    
    def modificar_libro(self, id, titulo, precio, editorial_id, autor_id):
        self.model.modificar_registro(id, {"titulo": titulo, "precio": precio, "editorial_id": editorial_id, "autor_id": autor_id})
        self.listar_libros()