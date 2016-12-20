from functools import wraps
from flask import g, url_for, redirect,request


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        return f(*args, **kwargs)
    return decorated_function
