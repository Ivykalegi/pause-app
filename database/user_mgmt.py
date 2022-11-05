import bcrypt
from database.db_mgmt import get_db_connection


def get_user_by_id(user_id):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, username, email
                                FROM users
                               WHERE id = %s""", [user_id])
            user = cursor.fetchone()
            return user


def create_new_user(username, email, password):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            password_bytes = password.encode()
            hashed_password = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
            cursor.execute("""INSERT 
                                INTO users
                                     (username, email, hashed_password)
                              VALUES (%s, %s, %s)""", [username, email, hashed_password])
            connection.commit()
            return cursor.lastrowid


def authenticate_user(username, password):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            password_bytes = password.encode()
            cursor.execute("""SELECT id, username, email, hashed_password
                                FROM users
                               WHERE username = %s""", [username])
            user = cursor.fetchone()
            if user and bcrypt.checkpw(password_bytes, user.get('hashed_password')):
                return user


def username_exists(username):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, username, email
                                FROM users
                               WHERE username = %s""", [username])
            user = cursor.fetchone()
            return True if user is None else False


def email_exists(email):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, username, email 
                                FROM users
                               WHERE email = %s""", [email])
            user = cursor.fetchone()
            return True if user is None else False
