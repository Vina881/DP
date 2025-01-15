from flask import redirect, url_for, render_template, flash
from Models.Book import Book
from App.Builder.BookBuilder import LibraryBookBuilder, BookDirector
from App.Factory.BookFactory import BookFactory
from App.Commands.BookCommands import ReserveBookCommand, ReturnBookCommand
from App.Strategy.SearchStrategy import SearchContext

class BookController:
    def __init__(self):
        self.book_builder = LibraryBookBuilder()
        self.book_director = BookDirector(self.book_builder)
        self.book_factory = BookFactory()
        self.search_context = SearchContext()

    def index(self, search_query, search_type, page):
        if search_query:
            self.search_context.set_strategy(search_type)
            books = self.search_context.execute_search(search_query)
        else:
            books = Book().paginate(page)
        return render_template('books/index.html', books=books)

    def show(self, id):
        book = Book().find(id)
        return render_template('books/show.html', book=book)

    def create(self, form_data):
        if form_data['type'] == 'textbook':
            book = self.book_director.create_textbook(
                form_data['title'],
                form_data['author'],
                form_data['isbn']
            )
        else:
            book = self.book_director.create_novel(
                form_data['title'],
                form_data['author'],
                form_data['isbn']
            )
        book.save()
        flash('Book created successfully', 'success')
        return redirect(url_for('books.index'))

    def import_books(self, book_data_list):
        imported_books = []
        for book_data in book_data_list:
            book = self.book_builder\
                .set_basic_info(book_data['title'], book_data['author'], book_data['isbn'])\
                .set_publication_info(book_data['publisher'], book_data['year'])\
                .set_category(book_data['category'])\
                .set_location(book_data['shelf'], book_data['row'])\
                .build()
            book.save()
            imported_books.append(book)
        return imported_books

    def reserve(self, id):
        command = ReserveBookCommand(id)
        try:
            command.execute()
            flash('Book reserved successfully', 'success')
        except ValueError as e:
            flash(str(e), 'error')
        return redirect(url_for('books.index'))

    def return_book(self, id):
        command = ReturnBookCommand(id)
        try:
            command.execute()
            flash('Book returned successfully', 'success')
        except ValueError as e:
            flash(str(e), 'error')
        return redirect(url_for('books.index'))
