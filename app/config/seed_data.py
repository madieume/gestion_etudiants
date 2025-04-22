# C’est un fichier Python qu’on utilise généralement pour remplir automatiquement une base de données avec des données de dé


from models.etudiant import Etudiant
from models.utilisateur import Utilisateur

etudiant = Etudiant("Ndiaye", "Bouba", "779856321", "L3 Physique", {"devoir": 17, "projet": 18, "examen": 16})
etudiants_collection.insert_one(etudiant.to_dict())

utilisateur = Utilisateur("Admin", "admin@example.com", "1234", "admin")
utilisateurs_collection.insert_one(utilisateur.to_dict())




























# from models.etudiant import Etudiant
# from models.utilisateur import Utilisateur
# from config.connexion import DatabaseConnexion  # Assure-toi que le chemin est bon

# # Connexion à la base
# db_connection = DatabaseConnexion()
# db = db_connection.get_mongo_db("gestion_etudiants")

# # Récupération des collections
# etudiants_collection = db["etudiants"]
# utilisateurs_collection = db["utilisateurs"]

# # Création d'un étudiant
# etudiant = Etudiant("Ndiaye", "Bouba", "779856321", "L3 Physique", {"devoir": 17, "projet": 18, "examen": 16})
# etudiants_collection.insert_one(etudiant.to_dict())

# # Création d'un utilisateur
# utilisateur = Utilisateur("Admin", "admin@example.com", "1234", "admin")
# utilisateurs_collection.insert_one(utilisateur.to_dict())

# print("✅ Données insérées avec succès !")