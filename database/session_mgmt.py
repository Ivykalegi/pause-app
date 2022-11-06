from database.db_mgmt import get_db_connection


def insert_user_session(user_id, start_datetime, duration_in_minutes):
    """
    Adds a new user session into the database

    *(Tables involved: sessions)*

    :param user_id: the user id of the user to add
    :type user_id: int
    :param start_datetime: the start datetime of user began the study session
    :type start_datetime: datetime
    :param duration_in_minutes: the time in minutes the study session lasted
    :type duration_in_minutes: int
    :rtype: None
    """
    with get_db_connection() as connection:
        with connection.cursor(dictionary=True) as cursor:
            cursor.execute("""INSERT 
                                INTO sessions
                                     (user_id, start_datetime, duration_in_minutes)
                              VALUES (%s, %s, %s)""", [user_id, start_datetime, duration_in_minutes])
            connection.commit()
