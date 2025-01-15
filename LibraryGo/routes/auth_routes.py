# Authentication Routes - Implementing Chain of Responsibility Pattern
from flask import Blueprint, request, redirect, render_template, flash, session
from Controllers.AuthController import AuthController
from App.Decorators import redirect_if_logged_in, performance_logger

auth_routes = Blueprint('auth', __name__)
auth_controller = AuthController()

@auth_routes.route('/login', methods=['GET', 'POST'])
@redirect_if_logged_in
@performance_logger
def login():
    if request.method == 'POST':
        return auth_controller.login(request.form)
    return render_template('auth/login.html')

@auth_routes.route('/register', methods=['GET', 'POST'])
@redirect_if_logged_in
@performance_logger
def register():
    if request.method == 'POST':
        return auth_controller.register(request.form)
    return render_template('auth/register.html')

@auth_routes.route('/logout')
def logout():
    session.clear()
    flash('Successfully logged out', 'success')
    return redirect('/login')