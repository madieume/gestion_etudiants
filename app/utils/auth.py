import bcrypt
import uuid
from ..config.connexion import DatabaseConnexion

class Auth:
    def __init__(self, db_connection: DatabaseConnexion):
        self.db_connection = db_connection

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, stored_hash, password):
        return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

   
