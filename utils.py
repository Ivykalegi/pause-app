from flask import request, redirect

from user_mgmt import username_exists, email_exists


def grab_form_values(*keys):
    if len(keys) == 1:
        return request.form.get(keys[0])
    return map(request.form.get, keys)


def grab_account_creation_error(username, display_name, email, pin):
    if not 1 <= len(username) <= 20:
        return 'Username must be between 1 and 20 characters long'
    if not username.isalnum():
        return 'Username must only include letters and numbers'
    if not 1 <= len(display_name) <= 20:
        return 'Display name must be between 1 and 20 characters long'
    if not 1 <= len(email) <= 50:
        return 'Email must be between 1 and 50 characters long'
    if not pin.isdigit() or len(pin) != 4:
        return 'Pin must consist of 4 digits'
    if not username_exists(username):
        return f'Username {username} is already taken'
    if not email_exists(email):
        return "An account with that email already exists.", 'error'