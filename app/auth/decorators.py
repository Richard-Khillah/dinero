from functools import wraps
from flask import g, url_for, redirect, request, abort

from app.auth import constants as USER


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function

def requres_status(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is USER.CUSTOMER:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function
