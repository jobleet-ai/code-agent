from .errors import ValidationError
from .validators import validate_username

_users = {}
_email_index = {}
_next_id = 1


def reset():
    global _next_id
    _users.clear()
    _email_index.clear()
    _next_id = 1


def create_user(username, email):
    global _next_id
    validate_username(username)
    if email in _email_index:
        raise ValidationError("email already registered")
    user = {"id": _next_id, "username": username, "email": email, "active": True}
    _users[_next_id] = user
    _email_index[email] = _next_id
    _next_id += 1
    return user


def get_user(user_id):
    return _users.get(user_id)


def update_user(user_id, **fields):
    user = _users[user_id]
    user.update(fields)
    return user


def delete_user(user_id):
    _users.pop(user_id, None)


def list_users():
    return list(_users.values())
