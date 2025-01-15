from flask import Blueprint, request, render_template, flash, redirect, url_for
from Controllers.BookController import BookController
from App.Decorator.LibraryDecorators import login_required, performance_logger

book_routes = Blueprint('books', __name__)
book_controller = BookController()

@book_routes.route('/books')
@login_required
@performance_logger
def index():
    search_query = request.args.get('search', '')
    search_type = request.args.get('type', 'title')
    page = int(request.args.get('page', 1))
    return book_controller.index(search_query, search_type, page)

@book_routes.route('/books/<int:id>')
@login_required
def show(id):
    return book_controller.show(id)

@book_routes.route('/books/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        return book_controller.create(request.form)
    return render_template('books/create.html')

@book_routes.route('/books/import', methods=['POST'])
@login_required
def import_books():
    if 'file' not in request.files:
        flash('No file uploaded', 'error')
        return redirect(url_for('books.index'))
    
    file = request.files['file']
    book_data_list = parse_book_data(file)
    imported_books = book_controller.import_books(book_data_list)
    flash(f'{len(imported_books)} books imported successfully', 'success')
    return redirect(url_for('books.index'))

@book_routes.route('/books/reserve/<int:id>', methods=['POST'])
@login_required
def reserve(id):
    return book_controller.reserve(id)

@book_routes.route('/books/return/<int:id>', methods=['POST'])
@login_required
def return_book(id):
    return book_controller.return_book(id)
