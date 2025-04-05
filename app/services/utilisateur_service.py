from ..models import Utilisateur

class UtilisateurService:
    def __init__(self):
        self.utilisateurs = []

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def authentifier_utilisateur(self, username, password):
        for utilisateur in self.utilisateurs:
            if utilisateur.username == username and utilisateur.password == password:
                return utilisateur
        return None