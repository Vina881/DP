# Decorator Pattern Implementation
from functools import wraps
from flask import session, redirect, url_for, request
import time
from typing import Callable

class BaseDecorator:
    def __init__(self, func):
        self.func = func
        wraps(func)(self)

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

class LoginRequired(BaseDecorator):
    def __call__(self, *args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('auth.login', next=request.url))
        return self.func(*args, **kwargs)

class AdminRequired(BaseDecorator):
    def __call__(self, *args, **kwargs):
        if 'user_id' not in session or session.get('role') != 'admin':
            return redirect(url_for('auth.login'))
        return self.func(*args, **kwargs)

class PerformanceLogger(BaseDecorator):
    def __call__(self, *args, **kwargs):
        start_time = time.time()
        result = self.func(*args, **kwargs)
        end_time = time.time()
        print(f"Function {self.func.__name__} took {end_time - start_time:.2f} seconds to execute")
        return result

# Decorator functions using the classes
def login_required(f: Callable) -> Callable:
    return LoginRequired(f)

def admin_required(f: Callable) -> Callable:
    return AdminRequired(f)

def performance_logger(f: Callable) -> Callable:
    return PerformanceLogger(f)
