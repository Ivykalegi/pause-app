from flask import Flask, request, flash, render_template, redirect, url_for, jsonify
from flask_login import LoginManager, UserMixin, login_user, logout_user, current_user, login_required
from datetime import datetime, timedelta

from config import FLASK_SECRET
from utils import grab_form_values, grab_account_creation_error

from database.user_mgmt import create_new_user, authenticate_user, get_user_by_id
from database.session_mgmt import insert_user_session

from api.pixela import create_graph, get_graph, add_session_to_graph

from activities.activity_manager import ActivityManager

port = 5004

app = Flask(__name__)
app.secret_key = FLASK_SECRET

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/signin'
login_manager.login_message = 'Please sign in to view this page.'
login_manager.login_message_category = 'error'

activity_manager = ActivityManager()


class User(UserMixin):

    def __init__(self, user_details):
        self.id = user_details.get('id')
        self.username = user_details.get('username')
        self.email = user_details.get('email')


@login_manager.user_loader
def user_loader(user_id):
    user_details = get_user_by_id(user_id)
    if user_details is None:
        return None
    user = User(user_details)
    return user


@app.get('/')
def home():
    if not current_user.is_anonymous:
        return redirect(url_for(view_dashboard.__name__))
    return render_template('home.html')


@app.get('/signin')
def view_signin():
    if not current_user.is_anonymous:
        return redirect(url_for(view_dashboard.__name__))
    return render_template('signin.html')


@app.post('/signin')
def accept_signin():
    if not current_user.is_anonymous:
        return redirect(url_for(view_dashboard.__name__))
    username, password = grab_form_values('username', 'password')
    user = authenticate_user(username, password)
    if user is None:
        flash('Invalid details, please try again', "error")
    else:
        user = User(user)
        login_user(user)
        return redirect(url_for(view_dashboard.__name__))
    return redirect(url_for(view_signin.__name__))


@app.get('/signup')
def view_signup():
    if not current_user.is_anonymous:
        return redirect(url_for(view_dashboard.__name__))
    return render_template('signup.html')


@app.post('/signup')
def accept_signup():
    if not current_user.is_anonymous:
        return redirect(url_for(view_dashboard.__name__))
    username, email, password = grab_form_values('username', 'email', 'password')
    if error := grab_account_creation_error(username, email, password):
        flash(error, "error")
        return redirect(url_for(view_signup.__name__))
    new_user_id = create_new_user(username, email, password)
    create_graph(new_user_id)
    flash("New account created.", "info")
    return redirect(url_for(view_signin.__name__))


@app.get('/signout')
@login_required
def accept_signout():
    logout_user()
    return redirect(url_for(home.__name__))


@app.get('/dashboard')
@login_required
def view_dashboard():
    return render_template('dashboard.html', user=current_user)


@app.get('/progress')
@login_required
def view_progress():
    graph = get_graph(current_user.id)
    return render_template('progress.html', user=current_user, graph=graph)


@app.get('/profile')
@login_required
def view_profile():
    return render_template('profile.html', user=current_user)


@app.get("/timer")
def view_timer():
    return render_template("timer.html", port=port)

@app.get("/how_pause_works")
def view_how_pause_works():
    return render_template("how_pause_works.html")

@app.post('/session')
def accept_session():
    end_datetime = request.json.get("end_datetime")
    duration_in_minutes = request.json.get("duration_in_minutes")
    start_datetime = datetime.strptime(end_datetime, '%Y-%m-%dT%H:%M:%S.%fZ') - timedelta(minutes=duration_in_minutes)
    insert_user_session(current_user.id, start_datetime, duration_in_minutes)
    add_session_to_graph(current_user.id, datetime.today(), duration_in_minutes)
    return jsonify(request.json)


@app.get("/activities")
def pick_activity():
    return activity_manager.get_random_activities()


if __name__ == "__main__":
    app.run(port=port)
