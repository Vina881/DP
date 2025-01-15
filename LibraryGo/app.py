from flask import Flask
from routes import register_routes
from config import Config
from App.Database.DatabaseConnection import DatabaseConnection
from App.Factory.BookFactory import BookFactory
from App.Factory.UserFactory import UserFactory
from App.Mediator.LibraryMediator import LibraryMediator
from App.Observer.NotificationObserver import NotificationSubject, EmailNotifier, SMSNotifier

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize Database
    db = DatabaseConnection()
    
    # Initialize Factories
    book_factory = BookFactory()
    user_factory = UserFactory()
    
    # Setup Mediator
    mediator = LibraryMediator()
    
    # Setup Observer Pattern for Notifications
    notification_subject = NotificationSubject()
    notification_subject.attach(EmailNotifier())
    notification_subject.attach(SMSNotifier())
    
    # Register all routes
    register_routes(app)
    
    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        db.rollback()
        return render_template('errors/500.html'), 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=Config.DEBUG)
