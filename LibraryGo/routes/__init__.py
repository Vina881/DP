# Route Registry - Implementing Facade Pattern for route management
from flask import Blueprint
from routes.auth_routes import auth_routes
from routes.book_routes import book_routes
from routes.admin_routes import admin_routes

def register_routes(app):
    app.register_blueprint(auth_routes)
    app.register_blueprint(book_routes)
    app.register_blueprint(admin_routes)