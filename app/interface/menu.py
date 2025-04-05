class Menu:
    def afficher_menu(self):
        print("1. Ajouter un étudiant")
        print("2. Rechercher un étudiant")
        print("3. Quitter")

    def choisir_option(self):
        return input("Choisir une option: ")
