# User Model - Implementing Observer and Strategy Patterns
from App.Database import DatabaseConnection
from werkzeug.security import generate_password_hash, check_password_hash

class User:
    def __init__(self):
        self.db = DatabaseConnection()

    def find(self, id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (id,))
        return cursor.fetchone()

    def find_by_email(self, email):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        return cursor.fetchone()

    def create(self, data):
        cursor = self.db.connection.cursor()
        cursor.execute(
            "INSERT INTO users (username, email, password, role) VALUES (%s, %s, %s, %s)",
            (data['username'], data['email'], 
             generate_password_hash(data['password']), data['role'])
        )
        self.db.connection.commit()
        return cursor.lastrowid

    def get_reservation_history(self, user_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("""
            SELECT r.*, b.title FROM reserve r 
            JOIN books b ON r.book_id = b.id 
            WHERE r.user_id = %s
            ORDER BY r.created_at DESC
        """, (user_id,))
        return cursor.fetchall()
