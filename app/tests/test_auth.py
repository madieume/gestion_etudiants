import unittest
from app.utils.auth import Auth
from app.config.connexion import DatabaseConnection

class TestAuth(unittest.TestCase):
    def test_hash_password(self):
        db_connection = DatabaseConnection('mongo_uri')
        auth = Auth(db_connection)
        password = "password123"
        hashed_password = auth.hash_password(password)
        self.assertTrue(auth.check_password(hashed_password, password))

if __name__ == '__main__':
    unittest.main()