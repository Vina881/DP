# Mediator Pattern Implementation
class LibraryMediator:
    def __init__(self):
        self.book_manager = None
        self.user_manager = None
        self.notification_service = None

    def process_reservation(self, book_id, user_id):
        if self.book_manager.is_available(book_id):
            if self.user_manager.can_reserve(user_id):
                self.book_manager.reserve(book_id)
                self.notification_service.notify_reservation(user_id)
                return True
        return False
