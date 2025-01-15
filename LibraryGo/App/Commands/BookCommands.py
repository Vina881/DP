# Command Pattern Implementation
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class ReserveBookCommand(Command):
    def __init__(self, book_id, user_id):
        self.book_id = book_id
        self.user_id = user_id

    def execute(self):
        book = Book().find(self.book_id)
        if book.state.can_reserve():
            Reserve().create(self.user_id, self.book_id)
            book.change_state(ReservedState())
            return True
        raise ValueError("Book cannot be reserved")

class ReturnBookCommand(Command):
    def __init__(self, book_id, user_id):
        self.book_id = book_id
        self.user_id = user_id

    def execute(self):
        book = Book().find(self.book_id)
        Reserve().cancel(self.book_id)
        book.change_state(AvailableState())
