# Composite Pattern Implementation
from abc import ABC, abstractmethod
from typing import List

class LibraryComponent(ABC):
    @abstractmethod
    def display(self) -> dict:
        pass

class CategoryComposite(LibraryComponent):
    def __init__(self, name: str):
        self.name = name
        self.children: List[LibraryComponent] = []

    def add(self, component: LibraryComponent):
        self.children.append(component)

    def remove(self, component: LibraryComponent):
        self.children.remove(component)

    def display(self) -> dict:
        return {
            'name': self.name,
            'type': 'category',
            'children': [child.display() for child in self.children]
        }

class BookLeaf(LibraryComponent):
    def __init__(self, book_data: dict):
        self.data = book_data

    def display(self) -> dict:
        return {
            'type': 'book',
            'data': self.data
        }
