# Factory Pattern Implementation
from abc import ABC, abstractmethod

class BookCreator(ABC):
    @abstractmethod
    def create_book(self, data):
        pass

class PhysicalBookCreator(BookCreator):
    def create_book(self, data):
        return PhysicalBook(data)

class DigitalBookCreator(BookCreator):
    def create_book(self, data):
        return DigitalBook(data)

class BookFactory:
    @staticmethod
    def get_creator(book_type):
        creators = {
            'physical': PhysicalBookCreator(),
            'digital': DigitalBookCreator()
        }
        return creators[book_type]
