# Reserve Model - Implementing State Pattern
from App.Database import DatabaseConnection
from datetime import datetime, timedelta

class Reserve:
    def __init__(self):
        self.db = DatabaseConnection()

    def create(self, user_id, book_id):
        cursor = self.db.connection.cursor()
        expiry_date = datetime.now() + timedelta(days=14)
        cursor.execute(
            "INSERT INTO reserve (user_id, book_id, status, expiry_date) VALUES (%s, %s, 'active', %s)",
            (user_id, book_id, expiry_date)
        )
        self.db.connection.commit()

    def get_active_reservations(self, user_id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM reserve WHERE user_id = %s AND status = 'active'",
            (user_id,)
        )
        return cursor.fetchall()

    def cancel(self, reserve_id):
        cursor = self.db.connection.cursor()
        cursor.execute(
            "UPDATE reserve SET status = 'cancelled' WHERE id = %s",
            (reserve_id,)
        )
        self.db.connection.commit()
