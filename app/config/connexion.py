import pymongo


class DatabaseConnexion:
    def __init__(self, mongo_uri="mongodb://localhost:27017/"):
        # Connexion à MongoDB
        self.mongo_client = pymongo.MongoClient(mongo_uri)
      

    def get_mongo_db(self, db_name):
        """
        Retourne la base de données MongoDB spécifiée.
        """
        return self.mongo_client[db_name]

 