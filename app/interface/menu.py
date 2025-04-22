class Menu:
    def afficher_menu(self):
        print("1. Ajouter un étudiant")
        print("2. Rechercher un étudiant")
        print("3. Modifier un étudiant")
        print("4. Supprimer un étudiant")
        print("5. Quitter")

    def choisir_option(self):
        return input("Choisir une option: ")
