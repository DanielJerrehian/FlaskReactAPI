from flask import request, abort
from functools import wraps


def validate_request_body(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    data = request.get_json()
    if not data:
        abort(400)
    else:
        for key, value in data.items():
            if value == "":
                data[key] = None
    return f(*args, **kwargs)
  return decorated_function