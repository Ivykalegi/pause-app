import bcrypt
from database.db_mgmt import get_db_connection


def get_user_by_id(user_id):
    """
    Gets the details of a specific user

    *(Tables involved: users)*

    :param user_id: the id of the user to get details for
    :type user_id: int
    :rtype: dict
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, username, email
                                FROM users
                               WHERE id = %s""", [user_id])
            user = cursor.fetchone()
            return user


def create_new_user(username, email, password):
    """
    Adds a new user to the database

    *(Tables involved: users)*

    :param username: the username of the user to add
    :type username: str
    :param email: the email of the user to add
    :type email: str
    :param password: the password of the user to add
    :type password: str
    :rtype: int
    """
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
    """
    Finds the user with a specific username and password combination.

    *(Tables involved: users)*

    :param username: the username of the user
    :type username: str
    :param password: the password of the user
    :type password: str
    :return: the user if found
    :rtype: dict or None
    """
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
    """
    Finds whether a particular username already exists in the database.

    *(Tables involved: users)*

    :param username: the username to check the availability of
    :type username: str
    :return: <code>True</code> if the username is available, or <code>False</code> otherwise
    :rtype: bool
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, username, email
                                FROM users
                               WHERE username = %s""", [username])
            user = cursor.fetchone()
            return True if user is None else False


def email_exists(email):
    """
    Finds whether a particular email already exists in the database.

    *(Tables involved: users)*

    :param email: the email to check the availability of
    :type email: str
    :return: <code>True</code> if the email is available, or <code>False</code> otherwise
    :rtype: bool
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, username, email 
                                FROM users
                               WHERE email = %s""", [email])
            user_email = cursor.fetchone()
            return True if user_email is None else False
