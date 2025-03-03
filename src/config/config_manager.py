import os
from dotenv import load_dotenv

class ConfigManager:
    def __init__(self):
        load_dotenv("config.env")

    def get_database_config(self):
        return {
            "host": os.getenv("DB_HOST"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "database": os.getenv("DB_NAME"),
            "use_pure": os.getenv("DB_USE_PURE")
        }
    
    def set_database(self, new_database):
        os.environ["DB_NAME"] = new_database
        print(f"Base de datos cambiada a: {new_database}")