from abc import ABC, abstractmethod
from Models.Book import Book

class BookBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def set_basic_info(self, title, author, isbn):
        pass

    @abstractmethod
    def set_publication_info(self, publisher, year):
        pass

    @abstractmethod
    def set_category(self, category):
        pass

    @abstractmethod
    def set_location(self, shelf, row):
        pass

class LibraryBookBuilder(BookBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.book = Book()

    def set_basic_info(self, title, author, isbn):
        self.book.title = title
        self.book.author = author
        self.book.isbn = isbn
        return self

    def set_publication_info(self, publisher, year):
        self.book.publisher = publisher
        self.book.year = year
        return self

    def set_category(self, category):
        self.book.category = category
        return self

    def set_location(self, shelf, row):
        self.book.shelf = shelf
        self.book.row = row
        return self

    def build(self):
        book = self.book
        self.reset()
        return book

class BookDirector:
    def __init__(self, builder: BookBuilder):
        self.builder = builder

    def create_textbook(self, title, author, isbn):
        return self.builder\
            .set_basic_info(title, author, isbn)\
            .set_category("Textbook")\
            .set_location("A", "1")\
            .build()

    def create_novel(self, title, author, isbn):
        return self.builder\
            .set_basic_info(title, author, isbn)\
            .set_category("Novel")\
            .set_location("B", "2")\
            .build()
