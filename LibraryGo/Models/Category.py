# Category Model - Implementing Composite Pattern
from App.Database import DatabaseConnection

class Category:
    def __init__(self):
        self.db = DatabaseConnection()

    def get_hierarchy(self):
        cursor = self.db.connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM categories")
        categories = cursor.fetchall()
        return self._build_tree(categories)

    def _build_tree(self, categories, parent_id=None):
        tree = []
        for category in categories:
            if category['parent_id'] == parent_id:
                children = self._build_tree(categories, category['id'])
                if children:
                    category['children'] = children
                tree.append(category)
        return tree

    def add(self, name, parent_id=None):
        cursor = self.db.connection.cursor()
        cursor.execute(
            "INSERT INTO categories (name, parent_id) VALUES (%s, %s)",
            (name, parent_id)
        )
        self.db.connection.commit()
