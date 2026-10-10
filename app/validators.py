from .errors import ValidationError

VALID_PRIORITIES = {"low", "medium", "high"}


def validate_username(username):
    if not username or not username.isalnum() or not (3 <= len(username) <= 20):
        raise ValidationError("username must be 3-20 alphanumeric characters")
    return username
