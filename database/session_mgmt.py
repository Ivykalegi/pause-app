from database.db_mgmt import get_db_connection


def insert_user_session(user_id, start_datetime, duration_in_minutes):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT 
                                INTO sessions
                                     (user_id, start_datetime, duration_in_minutes)
                              VALUES (%s, %s, %s)""", [user_id, start_datetime, duration_in_minutes])
            connection.commit()


def get_user_session(username):
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""SELECT id, username, week_day, start_time, end_time, total_hours
                                FROM study_sessions
                               WHERE username = %s""", [username])
            user = cursor.fetchone()
            return True if user is None else False


def update_user_session():
    pass


def delete_user_session():
    pass



def complete_session():
    pass