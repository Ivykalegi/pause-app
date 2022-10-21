from flask import request

from database.user_mgmt import username_exists, email_exists


def grab_form_values(*keys):
    if len(keys) == 1:
        return request.form.get(keys[0])
    return map(request.form.get, keys)


def grab_account_creation_error(username, email, password):
    if not 1 <= len(username) <= 20:
        return 'Username must be between 1 and 20 characters long'
    if not username.isalnum():
        return 'Username must only include letters and numbers'
    if not 1 <= len(email) <= 50:
        return 'Email must be between 1 and 50 characters long'
    if len(password) < 8:
        return 'Password must be at least 8 characters'
    if not username_exists(username):
        return f'Username {username} is already taken'
    if not email_exists(email):
        return "An account with that email already exists."
