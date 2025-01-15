# Singleton Pattern Implementation
import mysql.connector
from config import Config

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.connection = mysql.connector.connect(
                host=Config.DB_HOST,
                user=Config.DB_USER,
                password=Config.DB_PASSWORD,
                database=Config.DB_NAME
            )
        return cls._instance

    def get_cursor(self):
        return self.connection.cursor(dictionary=True)

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()
