class Etudiant:
    def __init__(self, nom, prenom, telephone, classe, notes):
        self.nom = nom
        self.prenom = prenom
        self.telephone = telephone
        self.classe = classe
        self.notes = notes  # Dictionnaire avec 'devoir', 'projet', 'examen'
        self.moyenne = self.calculer_moyenne()

    def calculer_moyenne(self):
        devoir = self.notes.get("devoir", 0)
        projet = self.notes.get("projet", 0)
        examen = self.notes.get("examen", 0)
        return round((devoir + projet + examen) / 3, 2)

    def to_dict(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "telephone": self.telephone,
            "classe": self.classe,
            "notes": self.notes,
            "moyenne": self.moyenne
        }
