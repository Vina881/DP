# Library Controller - Implementing Facade Pattern for library operations
from Models.Book import Book
from Models.User import User
from App.Mediator.LibraryMediator import LibraryMediator

class LibraryController:
    def __init__(self):
        self.book_model = Book()
        self.user_model = User()
        self.mediator = LibraryMediator()

    def handle_reservation(self, book_id, user_id):
        return self.mediator.process_reservation(book_id, user_id)

    def handle_return(self, book_id, user_id):
        return self.mediator.process_return(book_id, user_id)

    def get_user_history(self, user_id):
        return self.user_model.get_reservation_history(user_id)

    def get_book_status(self, book_id):
        return self.book_model.get_detailed_status(book_id)
