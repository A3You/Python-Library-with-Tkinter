from .BaseModel import BaseModel

class Autores(BaseModel):
    def __init__(self):
        super().__init__("autores")

    def listar_autores(self):
        consulta = "SELECT * FROM autores"
        return self.ejecutar_consulta(consulta, fetch=True)
    
    def mostrar_autor(self, id):
        consulta = "SELECT * FROM autores WHERE id = %s"
        return self.ejecutar_consulta(consulta, (id,), fetch=True)
    
    def crear_autor(self, nombre, apellidos, nacionalidad, fecha_nacimiento, fecha_fallecimiento=None):
        conexion = self._get_connection()
        if not conexion:
            raise ConnectionError("Error de conexión a la base de datos")
        
        try:
            cursor = conexion.cursor()
            consulta = "INSERT INTO autores (nombre, apellidos, nacionalidad, fecha_nacimiento, fecha_fallecimiento) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(consulta, (nombre, apellidos, nacionalidad, fecha_nacimiento, fecha_fallecimiento))
            autor_id = cursor.lastrowid
            conexion.commit()
            return autor_id

        except Exception as e:
            conexion.rollback()
            print(f"Error: {e}")
            raise  
        finally:
            cursor.close()
            conexion.close()
    
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


    
    def eliminar_autor(self, id):
        consulta = "DELETE FROM libros_autores WHERE id_autor = %s; DELETE FROM autores WHERE id = %s;"
        return self.ejecutar_consulta(consulta, (id, id))

    def modificar_registro(self, id, nuevos_datos):
        consulta_autor = """
            UPDATE autores 
            SET nombre = %s, 
                apellidos = %s, 
                nacionalidad = %s, 
                fecha_nacimiento = %s, 
                fecha_fallecimiento = %s
            WHERE id = %s
        """
        valores_autor = (
            nuevos_datos["nombre"],
            nuevos_datos["apellidos"],
            nuevos_datos["nacionalidad"],
            nuevos_datos["fecha_nacimiento"],
            nuevos_datos.get("fecha_fallecimiento"),
            id
        )
        self.ejecutar_consulta(consulta_autor, valores_autor)
