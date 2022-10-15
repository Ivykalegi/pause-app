import bcrypt
from db_management import get_db_connection


def get_user_id(user_id):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, username, email
                                FROM logininfo
                               WHERE id = %s""", [user_id])
            user = cursor.fetchone()
            return user


def create_new_user(username, display_name, email, pin):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            pin_bytes = pin.encode()
            hashed_pin = bcrypt.hashpw(pin_bytes, bcrypt.gensalt())
            cursor.execute("""INSERT 
                                INTO logininfo
                                     (username, display_name, email, hashed_pin)
                              VALUES (%s, %s, %s, %s)""", [username, display_name, email, hashed_pin])
            connection.commit()


def get_user_details(username, email, pin):   #username or email
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            pin_bytes = pin.encode()
            cursor.execute("""SELECT id, username, email, hashed_pin
                                FROM logininfo
                               WHERE username = %s
                                 AND email = %s""", [username, email])
            user = cursor.fetchone()
            if user and bcrypt.checkpw(pin_bytes, user.get('hashed_pin')):
                return user


def username_exists(username):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT *
                                FROM logininfo
                               WHERE username = %s""", [username])
            user = cursor.fetchone()
            return True if user is None else False


def email_exists(email):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, username, email 
                                FROM login_info
                               WHERE email = %s""", [email])
            user = cursor.fetchone()
            return True if user is None else False
