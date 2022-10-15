from flask import Flask, request, flash, make_response, render_template, redirect, session, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required

from config import FLASK_SECRET, FLASK_DEBUG
from db_management import get_db_connection
from utils import grab_form_values, grab_account_creation_error
from user_mgmt import create_new_user, get_user_details, get_user_id

app = Flask(__name__)
app.secret_key = FLASK_SECRET

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/signin'
login_manager.login_message = 'Please sign in to view this page.'


class User(UserMixin):

    def __init__(self, user_details):
        self.id = user_details.get('id')
        self.name = user_details.get('name')
        self.email = user_details.get('email')


@login_manager.user_loader
def user_loader(user_id):
    user_details = get_user_id(user_id)
    if user_details is None:
        return None
    user = User(user_details)
    return user


@app.get('/')
def home():
    return render_template('home.html')


@app.get('/signin')
def view_signin():
    if not current_user.is_anonymous:
        return make_response(redirect(url_for(view_profile.__name__)))
    return render_template('signin.html')


@app.post('/signin')
def accept_signin():
    if not current_user.is_anoymous:
        return make_response(redirect(url_for(view_profile.__name__)))
    username, pin = grab_form_values('username', 'pin')
    response = make_response(redirect(url_for(view_signin.__name__)))
    user = get_user_details(username, pin)
    if user is None:
        flash('Invalid details, please try again')
    else:
        user = User(user)
        login_user(user)
        return make_response(redirect(url_for(view_profile.__name__)))
    return response


@app.get('/signup')
def view_signup():
    if not current_user.is_anonymous:
        return make_response(redirect(url_for(view_profile.__name__)))
    return render_template('signup.html')


@app.post('/signup')
def accept_signup():
    if not current_user.is_anoymous:
        return make_response(redirect(url_for(view_profile.__name__)))
    username, display_name, email, pin = grab_account_creation_error('username', 'display_name', 'email', 'pin')
    if error := grab_account_creation_error(username, display_name, email, pin):
        flash(error)
        return redirect(url_for(view_signup.__name__))
    create_new_user(username, display_name, email, pin)
    flash("New account created.")
    return redirect(url_for(view_signup.__name__))


@app.post('/signout')
@login_required
def accept_logout():
    logout_user()
    response = make_response(redirect(url_for(view_signin.__name__)))
    return response


@app.get('/profile')
@login_required
def view_profile():
    return render_template('profile.html', user=current_user)


@app.get("/")
def timer():
    return render_template("timer.html")


if __name__ == "__main__":
    app.run(port=5001)
