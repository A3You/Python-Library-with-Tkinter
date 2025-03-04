from .BaseModel import BaseModel

class Libro(BaseModel):
    def __init__(self):
        super().__init__("libros")

    def listar_todos(self):
        consulta = """
            SELECT libros.id, libros.titulo, libros.precio, libros.id_editorial, 
            (SELECT GROUP_CONCAT(apellidos, ', ', nombre SEPARATOR '; ') FROM autores WHERE id IN (SELECT id_autor FROM libros_autores WHERE id_libro = libros.id)) AS autores,
            (SELECT nombre FROM editoriales WHERE id = libros.id_editorial) AS editorial
            FROM libros
        """
        return self.ejecutar_consulta(consulta, fetch=True)