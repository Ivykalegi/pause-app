import mysql.connector
from config import DB_HOST, DB_NAME, DB_PASS, DB_USER


def get_db_connection():
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME)
    return connection
