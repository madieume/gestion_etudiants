import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from app.interface.menu import Menu  # Assure-toi du bon chemin d'importation

def main():
    menu = Menu()
    menu.afficher_menu()
    choix = menu.choisir_option()

    if choix == "1":
        # Ajouter un étudiant
        pass
    elif choix == "2":
        # Rechercher un étudiant
        pass
    elif choix == "3":
        print("Quitter")
        exit()

if __name__ == "__main__":
    main()
