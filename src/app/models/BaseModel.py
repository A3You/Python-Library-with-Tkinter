import mysql.connector
from config.config_manager import ConfigManager

class BaseModel:
    def __init__(self, tabla):
        self.config = ConfigManager().get_database_config()
        self.tabla = tabla
        # No inicialices la conexión aquí
    
    def _get_connection(self):
        """Crea una nueva conexión para cada operación."""
        try:
            return mysql.connector.connect(**self.config)
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            return None

    def ejecutar_consulta(self, consulta, valores=None, fetch=False, dictionary=True, commit=True):
        conexion = self._get_connection()
        if not conexion:
            return None

        cursor = conexion.cursor(dictionary=dictionary)
        try:
            if valores:
                cursor.execute(consulta, valores)
            else:
                cursor.execute(consulta)
            
            if fetch:
                resultado = cursor.fetchall()
            else:
                if commit:  # Nuevo parámetro para controlar el commit
                    conexion.commit()
                resultado = cursor.lastrowid

            return resultado
        except mysql.connector.Error as err:
            print(f"Error en la consulta: {err}")
            conexion.rollback()  # Rollback en caso de error
            return None
        finally:
            cursor.close()
            conexion.close()

    def crear_registro(self, datos):
        """
        Inserta un nuevo registro en la tabla.
        datos: Diccionario con los valores a insertar. 
        """
        columnas = ", ".join(datos.keys())
        valores = tuple(datos.values())
        marcadores = ", ".join(["%s"] * len(datos))

        consulta = f"INSERT INTO {self.tabla} ({columnas}) VALUES ({marcadores})"
        return self.ejecutar_consulta(consulta, valores)

    def listar_todos(self):
        """
        Obtiene todos los registros de la tabla.
        """
        consulta = f"SELECT * FROM {self.tabla}"
        return self.ejecutar_consulta(consulta, fetch=True)

    def buscar_por_id(self, id):
        """
        Busca un registro por ID.
        """
        consulta = f"SELECT * FROM {self.tabla} WHERE id = %s"
        resultado = self.ejecutar_consulta(consulta, (id,), fetch=True)

        return resultado[0] if resultado else None

    def modificar_registro(self, id, nuevos_datos):
        """
        Modifica un registro existente.
        nuevos_datos: Diccionario con los valores a actualizar. Ejemplo:
        {"nombre": "Nuevo Nombre", "edad": 35}
        """
        columnas = ", ".join([f"{col} = %s" for col in nuevos_datos.keys()])
        valores = tuple(nuevos_datos.values()) + (id,)

        consulta = f"UPDATE {self.tabla} SET {columnas} WHERE id = %s"
        return self.ejecutar_consulta(consulta, valores)

    def eliminar_registro(self, id):
        """
        Elimina un registro por ID.
        """
        consulta = f"DELETE FROM {self.tabla} WHERE id = %s"
        return self.ejecutar_consulta(consulta, (id,))

    def cerrar_conexion(self):
        """
        Cierra la conexión con la base de datos.
        """
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")

