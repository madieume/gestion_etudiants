class Statistiques:
    @staticmethod
    def calculer_moyenne_globale(etudiants):
        total_moyennes = sum([e.moyenne() for e in etudiants])
        return total_moyennes / len(etudiants)

    @staticmethod
    def classement(etudiants):
        return sorted(etudiants, key=lambda x: x.moyenne(), reverse=True)
