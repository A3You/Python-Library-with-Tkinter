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
        conexion = self._get_connection()
        if not conexion:
            raise ConnectionError("Error de conexión a la base de datos")
        
        try:
            cursor = conexion.cursor()
            
            
            cursor.execute("SELECT id FROM editoriales WHERE id = %s", (editorial,))
            if not cursor.fetchone():
                raise ValueError(f"Editorial ID {editorial} no existe")

           
            if autores:
                placeholders = ','.join(['%s'] * len(autores))
                cursor.execute(f"SELECT id FROM autores WHERE id IN ({placeholders})", tuple(autores))
                autores_validos = {row[0] for row in cursor.fetchall()}
                
                if len(autores_validos) != len(autores):
                    invalidos = set(autores) - autores_validos
                    raise ValueError(f"Autores no válidos: {invalidos}")

           
            consulta_libro = """
                INSERT INTO libros (titulo, precio, id_editorial, fecha_publicacion) 
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(consulta_libro, (titulo, precio, editorial, fecha_publicacion))
            libro_id = cursor.lastrowid

            if autores:
                cursor.executemany(
                    "INSERT INTO libros_autores (id_libro, id_autor) VALUES (%s, %s)",
                    [(libro_id, autor_id) for autor_id in autores]
                )

            conexion.commit()
            return libro_id

        except Exception as e:
            conexion.rollback()
            print(f"Error: {e}")
            raise  
        finally:
            cursor.close()
            conexion.close()
    def mostrar_libro(self, id):
        consulta = """
            SELECT libros.id, libros.titulo, libros.precio, libros.id_editorial, libros.fecha_publicacion,
            (SELECT GROUP_CONCAT(autores.id, ':', apellidos, ', ', nombre SEPARATOR '; ') FROM autores WHERE id IN (SELECT id_autor FROM libros_autores WHERE id_libro = %s)) AS autores,
            (SELECT nombre FROM editoriales WHERE id = libros.id_editorial) AS editorial
            FROM libros
            WHERE libros.id = %s
        """
        return self.ejecutar_consulta(consulta, (id, id), fetch=True)
    
    def autores_libro(self, id_libro):
        if not isinstance(id_libro, list):
            consulta = """
                SELECT id_autor FROM libros_autores WHERE id_libro = %s
            """
            valores = (id_libro,)
        else:
            consulta = """
                SELECT id_autor FROM libros_autores WHERE id_libro IN %s
            """
            valores = (tuple(id_libro),)
        return self.ejecutar_consulta(consulta, valores, fetch=True)


    def listar_autores(self):
        consulta = "SELECT * FROM autores"
        return self.ejecutar_consulta(consulta, fetch=True)
    
    def mostrar_autor(self, id):
        consulta = "SELECT * FROM autores WHERE id = %s"
        return self.ejecutar_consulta(consulta, (id), fetch=True)
    
    def listar_editoriales(self):
        consulta = "SELECT id, nombre FROM editoriales"
        return self.ejecutar_consulta(consulta, fetch=True)
    
    def eliminar_registro(self, id):
        consulta = "DELETE FROM libros_autores WHERE id_libro = %s; DELETE FROM libros WHERE id = %s;"
        return self.ejecutar_consulta(consulta, (id, id))

    def modificar_registro(self, id, nuevos_datos):
        """
        Modifica un registro existente en la tabla 'libros' y actualiza los autores asociados.
        """
        consulta_libro = """
            UPDATE libros 
            SET titulo = %s, precio = %s, id_editorial = %s, fecha_publicacion = %s 
            WHERE id = %s
        """
        valores_libro = (
            nuevos_datos["titulo"],
            nuevos_datos["precio"],
            nuevos_datos["id_editorial"],
            nuevos_datos["fecha_publicacion"],
            id
        )
        self.ejecutar_consulta(consulta_libro, valores_libro)
        
        # Actualizar autores
        consulta_eliminar_autores = "DELETE FROM libros_autores WHERE id_libro = %s"
        self.ejecutar_consulta(consulta_eliminar_autores, (id,))
        
        consulta_insertar_autores = "INSERT INTO libros_autores (id_libro, id_autor) VALUES (%s, %s)"
        for autor_id in nuevos_datos["autores"]:
            self.ejecutar_consulta(consulta_insertar_autores, (id, autor_id))
