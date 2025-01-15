# Admin Controller - Implementing Template Method Pattern for reports
from Models.Book import Book
from Models.User import User
from App.Template.ReportGenerator import BookReportGenerator, UserReportGenerator
from flask import render_template

class AdminController:
    def __init__(self):
        self.book_model = Book()
        self.user_model = User()

    def dashboard(self):
        stats = {
            'total_books': self.book_model.count(),
            'total_users': self.user_model.count(),
            'active_reservations': self.book_model.count_active_reservations()
        }
        return render_template('admin/dashboard.html', stats=stats)

    def list_books(self):
        books = self.book_model.all()
        return render_template('admin/books.html', books=books)

    def list_users(self):
        users = self.user_model.all()
        return render_template('admin/users.html', users=users)

    def generate_report(self, report_type):
        generators = {
            'books': BookReportGenerator(),
            'users': UserReportGenerator()
        }
        report = generators[report_type].generate()
        return render_template('admin/reports.html', report=report)
