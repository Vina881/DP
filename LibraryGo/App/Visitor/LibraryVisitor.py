# Visitor Pattern Implementation
from abc import ABC, abstractmethod

class LibraryVisitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass

    @abstractmethod
    def visit_user(self, user):
        pass

class MaintenanceVisitor(LibraryVisitor):
    def visit_book(self, book):
        return {
            'id': book.id,
            'condition': book.condition,
            'last_maintenance': book.last_maintenance,
            'maintenance_due': book.calculate_next_maintenance()
        }

    def visit_user(self, user):
        return {
            'id': user.id,
            'active_reservations': len(user.get_active_reservations()),
            'account_status': user.check_account_status()
        }
