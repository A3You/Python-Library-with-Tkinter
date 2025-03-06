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
    
    def crear_libro(self, titulo, precio, editorial, fecha_publicacion, autores):
        consulta = """
            INSERT INTO libros (titulo, precio, id_editorial, fecha_publicacion) 
            VALUES (%s, %s, %s, %s);
        """
        libro_id = self.ejecutar_consulta(consulta, (titulo, precio, editorial, fecha_publicacion))
        
        for autor in autores:
            consulta_autor = """
            INSERT INTO libros_autores (id_libro, id_autor) 
            VALUES (%s, %s)
            """
            self.ejecutar_consulta(consulta_autor, (libro_id, autor))
    
    def mostrar_libro(self, id):
        consulta = """
            SELECT libros.id, libros.titulo, libros.precio, libros.id_editorial, libros.fecha_publicacion,
            (SELECT GROUP_CONCAT(apellidos, ', ', nombre SEPARATOR '; ') FROM autores WHERE id IN (SELECT id_autor FROM libros_autores WHERE id_libro = %s)) AS autores,
            (SELECT nombre FROM editoriales WHERE id = libros.id_editorial) AS editorial
            FROM libros
            WHERE libros.id = %s
        """
        return self.ejecutar_consulta(consulta, (id, id), fetch=True)


    def listar_autores(self):
        consulta = "SELECT id, apellidos, nombre FROM autores"
        return self.ejecutar_consulta(consulta, fetch=True)
    
    def listar_editoriales(self):
        consulta = "SELECT id, nombre FROM editoriales"
        return self.ejecutar_consulta(consulta, fetch=True)
    
    def eliminar_registro(self, id):
        consulta = "DELETE FROM libros_autores WHERE id_libro = %s; DELETE FROM libros WHERE id = %s;"
        return self.ejecutar_consulta(consulta, (id, id))

    def modificar_registro(self, id, nuevos_datos):
        # Incluye todos los campos necesarios
        consulta = """
            UPDATE libros 
            SET titulo = %s, precio = %s, id_editorial = %s, fecha_publicacion = %s 
            WHERE id = %s
        """
        valores = (
            nuevos_datos["titulo"],
            nuevos_datos["precio"],
            nuevos_datos["id_editorial"],
            nuevos_datos["fecha_publicacion"],
            id
        )
        return self.ejecutar_consulta(consulta, valores)
