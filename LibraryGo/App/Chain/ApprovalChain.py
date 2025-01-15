# Chain of Responsibility Pattern Implementation
class ApprovalHandler:
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None

class LibrarianApproval(ApprovalHandler):
    def handle(self, request):
        if request.book.is_regular():
            return "Approved by Librarian"
        return super().handle(request)

class AdminApproval(ApprovalHandler):
    def handle(self, request):
        if request.book.is_rare():
            return "Approved by Admin"
        return super().handle(request)
