# State Pattern Implementation
from abc import ABC, abstractmethod

class BookState(ABC):
    @abstractmethod
    def can_reserve(self) -> bool:
        pass

    @abstractmethod
    def get_status(self) -> str:
        pass

class AvailableState(BookState):
    def can_reserve(self) -> bool:
        return True

    def get_status(self) -> str:
        return 'available'

class ReservedState(BookState):
    def can_reserve(self) -> bool:
        return False

    def get_status(self) -> str:
        return 'reserved'
