# Admin Routes - Implementing Proxy Pattern for access control
from flask import Blueprint, request
from Controllers.AdminController import AdminController
from App.Decorators import admin_required, performance_logger

admin_routes = Blueprint('admin', __name__)
admin_controller = AdminController()

@admin_routes.route('/admin/dashboard')
@admin_required
@performance_logger
def dashboard():
    return admin_controller.dashboard()

@admin_routes.route('/admin/books', methods=['GET', 'POST'])
@admin_required
def manage_books():
    if request.method == 'POST':
        return admin_controller.create_book(request.form)
    return admin_controller.list_books()

@admin_routes.route('/admin/users')
@admin_required
def manage_users():
    return admin_controller.list_users()

@admin_routes.route('/admin/reports')
@admin_required
def reports():
    report_type = request.args.get('type', 'general')
    return admin_controller.generate_report(report_type)