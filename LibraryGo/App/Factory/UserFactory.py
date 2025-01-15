# Factory Pattern Implementation
class UserFactory:
    @staticmethod
    def create_user(role, data):
        users = {
            'member': Member,
            'librarian': Librarian,
            'admin': Admin
        }
        return users[role](data)
