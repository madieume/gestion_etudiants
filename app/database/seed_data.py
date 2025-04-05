from models.etudiant import Etudiant
from models.utilisateur import Utilisateur

etudiant = Etudiant("Ndiaye", "Bouba", "779856321", "L3 Physique", {"devoir": 17, "projet": 18, "examen": 16})
etudiants_collection.insert_one(etudiant.to_dict())

utilisateur = Utilisateur("Admin", "admin@example.com", "1234", "admin")
utilisateurs_collection.insert_one(utilisateur.to_dict())
