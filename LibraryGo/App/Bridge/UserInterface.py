# Bridge Pattern Implementation
from abc import ABC, abstractmethod

class UserInterface(ABC):
    def __init__(self, implementation):
        self.implementation = implementation

    @abstractmethod
    def show_book_details(self, book_id):
        pass

class WebInterface(UserInterface):
    def show_book_details(self, book_id):
        details = self.implementation.get_book_details(book_id)
        return render_template('books/show.html', book=details)

class MobileInterface(UserInterface):
    def show_book_details(self, book_id):
        details = self.implementation.get_book_details(book_id)
        return jsonify(details)
