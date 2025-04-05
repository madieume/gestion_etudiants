import pymongo
import redis

class DatabaseConnection:
    def __init__(self, mongo_uri="mongodb://localhost:27017/", redis_uri="redis://localhost:6379/"):
        # Connexion à MongoDB
        self.mongo_client = pymongo.MongoClient(mongo_uri)
        # Connexion à Redis
        self.redis_client = redis.StrictRedis.from_url(redis_uri)

    def get_mongo_db(self, db_name):
        """
        Retourne la base de données MongoDB spécifiée.
        """
        return self.mongo_client[db_name]

    def get_redis_db(self):
        """
        Retourne la connexion à Redis.
        """
        return self.redis_client