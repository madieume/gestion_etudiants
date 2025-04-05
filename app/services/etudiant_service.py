from ..models import Etudiant

class EtudiantService:
    def __init__(self):
        self.etudiants = []

    def ajouter_etudiant(self, etudiant):
        self.etudiants.append(etudiant)

    def rechercher_etudiant(self, nom):
        return [e for e in self.etudiants if nom.lower() in e.nom.lower()]

    def modifier_etudiant(self, etudiant, nouveau_nom):
        etudiant.nom = nouveau_nom

    def supprimer_etudiant(self, etudiant):
        self.etudiants.remove(etudiant)
