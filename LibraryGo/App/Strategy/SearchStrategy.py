# Strategy Pattern Implementation
from abc import ABC, abstractmethod
from typing import List, Dict

class SearchStrategy(ABC):
    @abstractmethod
    def search(self, query: str, books: List[Dict]) -> List[Dict]:
        pass

class TitleSearch(SearchStrategy):
    def search(self, query: str, books: List[Dict]) -> List[Dict]:
        return [book for book in books if query.lower() in book['title'].lower()]

class AuthorSearch(SearchStrategy):
    def search(self, query: str, books: List[Dict]) -> List[Dict]:
        return [book for book in books if query.lower() in book['author'].lower()]

class ISBNSearch(SearchStrategy):
    def search(self, query: str, books: List[Dict]) -> List[Dict]:
        return [book for book in books if query == book['isbn']]

class SearchContext:
    def __init__(self):
        self._strategy = TitleSearch()

    def set_strategy(self, search_type: str):
        strategies = {
            'title': TitleSearch(),
            'author': AuthorSearch(),
            'isbn': ISBNSearch()
        }
        self._strategy = strategies[search_type]

    def execute_search(self, query: str, books: List[Dict]) -> List[Dict]:
        return self._strategy.search(query, books)
