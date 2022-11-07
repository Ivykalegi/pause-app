import unittest
import unittest.mock
import database.user_mgmt


def get_mock_db_cursor(fetchone_return_value=None, fetchall_return_value=None):
    return unittest.mock.Mock(
        __enter__=lambda _: unittest.mock.Mock(
            execute=lambda query, params: None,
            fetchone=lambda: fetchone_return_value,
            fetchall=lambda: fetchall_return_value,
        ),
        __exit__=lambda *args: None,
    )


def get_mock_db_connection(mock_db_cursor):
    return unittest.mock.Mock(
        __enter__=lambda _: unittest.mock.Mock(
            cursor=lambda **kwargs: mock_db_cursor,
        ),
        __exit__=lambda *args: None,
    )


class TestUserMgmt(unittest.TestCase):

    def test_user_by_id(self):
        mock_user_id = 1
        mock_user = {"id": 1, "username": "ivy", "email": "ivy@xyz.com"}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user)
        mock_db_connection= get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.user_mgmt.get_user_by_id(user_id=mock_user_id)
            self.assertEqual(result, mock_user)

    def test_authenticate_user_with_valid_login(self):
        mock_username = "jo"
        mock_password = "password2"
        mock_user = {"id": 2, "username": "jo", "email": "jo@xyz.com", "hashed_password": b'$2b$12$mARkeJr3alCi3DlxG59GNOPjJ4Jl666BAMF5WU1t9BV4Hf9y/y2I2'}
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.user_mgmt.authenticate_user(username=mock_username, password=mock_password)
            self.assertEqual(result, mock_user)

    def test_authenticate_user_with_invalid_login(self):
        mock_username = "randomperson"
        mock_password = "coolkid!"
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.user_mgmt.authenticate_user(username=mock_username, password=mock_password)
            self.assertIsNone(result)

    def test_email_exists_with_available_email(self):
        mock_email = "larissa@xyz.com"
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=None)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.user_mgmt.email_exists(email=mock_email)
            self.assertTrue(result)

    def test_email_exists_with_unavailable_email(self):
        mock_email = "larissa@xyz.com"
        mock_user_id = 3
        mock_db_cursor = get_mock_db_cursor(fetchone_return_value=mock_user_id)
        mock_db_connection = get_mock_db_connection(mock_db_cursor)
        with unittest.mock.patch("mysql.connector.connect", return_value=mock_db_connection):
            result = database.user_mgmt.email_exists(email=mock_email)
            self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
