class Utilisateur:
    def __init__(self, nom, email, mot_de_passe, role="enseignant"):
        self.nom = nom
        self.email = email
        self.mot_de_passe = mot_de_passe  # À chiffrer si besoin
        self.role = role

    def to_dict(self):
        return {
            "nom": self.nom,
            "email": self.email,
            "mot_de_passe": self.mot_de_passe,
            "role": self.role
        }
