# Book Model - Implementing State and Observer Patterns
from App.Database import DatabaseConnection
from App.State.BookState import AvailableState, ReservedState, BorrowedState
from datetime import datetime

class Book:
    def __init__(self):
        self.db = DatabaseConnection()
        self.state = AvailableState()
        self.observers = []

    def find(self, id):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books WHERE id = %s", (id,))
        return cursor.fetchone()

    def all(self):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books")
        return cursor.fetchall()

    def paginate(self, page, per_page=10):
        offset = (page - 1) * per_page
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM books LIMIT %s OFFSET %s", (per_page, offset))
        return cursor.fetchall()

    def change_state(self, new_state):
        self.state = new_state
        self._notify_observers()

    def add_observer(self, observer):
        self.observers.append(observer)

    def _notify_observers(self):
        for observer in self.observers:
            observer.update(self)

    def count_active_reservations(self):
        cursor = self.db.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM reserve WHERE status = 'active'")
        return cursor.fetchone()[0]
