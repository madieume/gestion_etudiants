import bcrypt
import uuid
from ..database.connection import DatabaseConnection

class Auth:
    def __init__(self, db_connection: DatabaseConnection):
        self.db_connection = db_connection

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, stored_hash, password):
        return bcrypt.checkpw(password.encode('utf-8'), stored_hash)

    def creer_session(self, utilisateur):
        session_id = str(uuid.uuid4())
        self.db_connection.get_redis_db().set(session_id, utilisateur.username)
        return session_id

    def verifier_session(self, session_id):
        return self.db_connection.get_redis_db().get(session_id)
