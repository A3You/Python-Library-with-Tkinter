import configparser
import mysql.connector

class ConfigManager:
    file = './config.ini'
    def __init__(self, config_file="config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_database_config(self):
        return {
            "host": self.config.get("database", "host", fallback="localhost"),
            "user": self.config.get("database", "user", fallback="root"),
            "password": self.config.get("database", "password", fallback="root"),
            "database": self.config.get("database", "database", fallback="bd_pylib"),
            "use_pure": self.config.getboolean("database", "use_pure", fallback=False)
        }
    
    def probar_conexion(self):
        """
        Prueba la conexión con la base de datos y devuelve un mensaje de éxito o error.
        """
        try:
            conexion = mysql.connector.connect(**self.get_database_config())
            if conexion.is_connected():
                print("Conexión exitosa.")
            else:
                print("No se pudo establecer la conexión.")
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
        finally:
            if 'conexion' in locals() and conexion.is_connected():
                conexion.close()

prueba = ConfigManager()
prueba.probar_conexion()

