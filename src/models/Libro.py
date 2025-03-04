from BaseModel import BaseModel
import _mysql_connector

class Libro(BaseModel):
    def __init__(self):
        super().__init__("libros")

    def listar_todos(self):
        consulta = """
            SELECT libros.id, libros.titulo, libros.precio, libros.editorial_id, libros.autor_id, 
            (SELECT nombre FROM autores WHERE id = libros.autor_id) AS autor,
            (SELECT nombre FROM editoriales WHERE id = l.editorial_id) AS editorial
            FROM libros l
        """
        return self.ejecutar_consulta(consulta, fetch=True)