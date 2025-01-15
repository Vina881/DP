# Authentication Controller - Implementing Strategy Pattern for different auth methods
from Models.User import User
from flask import session, redirect, url_for, flash
from App.Factory.UserFactory import UserFactory

class AuthController:
    def __init__(self):
        self.user_model = User()
        self.user_factory = UserFactory()

    def login(self, form_data):
        user = self.user_model.find_by_email(form_data['email'])
        if user and user.verify_password(form_data['password']):
            session['user_id'] = user.id
            session['role'] = user.role
            flash('Successfully logged in', 'success')
            return redirect(url_for('books.index'))
        flash('Invalid credentials', 'error')
        return redirect(url_for('auth.login'))

    def register(self, form_data):
        try:
            user = self.user_factory.create_user('member', form_data)
            session['user_id'] = user.id
            session['role'] = user.role
            flash('Registration successful', 'success')
            return redirect(url_for('books.index'))
        except ValueError as e:
            flash(str(e), 'error')
            return redirect(url_for('auth.register'))
