import os
import configparser
import mysql.connector

class ConfigManager:
    def __init__(self, config_file=os.path.join(os.path.dirname(__file__), 'config.ini')):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get_database_config(self):
        return {
            "host": self.config.get("database", "host"),
            "user": self.config.get("database", "user"),
            "password": self.config.get("database", "password"),  # Faltaba el parámetro "option"
            "database": self.config.get("database", "database"),  # Faltaba el parámetro "option"
            "use_pure": self.config.getboolean("database", "use_pure")
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

