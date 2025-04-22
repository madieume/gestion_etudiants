#  Gestion des étudiants

# Description
Ce projet est une application en Python permettant la **gestion des étudiants** d’un établissement.  
Les données sont stockées dans une base **MongoDB**.  
Elle permet d’ajouter, rechercher, modifier et supprimer les informations des étudiants et de générer des statistiques académiques.

---

# Fonctionnalités principales

- Enregistrement des étudiants
- Calcul des moyennes (devoir, projet, examen)
- Affichage des étudiants dans un tableau
- Recherche et modification des notes
- Exportation des données
- Interface terminale interactive
- Stockage des données avec MongoDB

---

# Technologies utilisées

- **Langage** : Python 
- **Base de données** : MongoDB
- **Bibliothèques** :
  - `pymongo` pour la connexion à MongoDB
  - `dotenv` pour la gestion du fichier `.env`
 

---

# Installation et lancement

1. Cloner le dépôt :
```bash
git clone https://github.com/madieume/gestion_etudiants.git
cd gestion_etudiants
```

2. Créer un environnement virtuel et l’activer :
```bash



3. Installer les dépendances :
```bash
pip install -r requirements.txt
```

4. Configurer la base MongoDB dans le fichier `.env` :
```
MONGO_URI=mongodb://localhost:27017
DB_NAME=gestion_etudiants
```

5. Lancer l’application :
```bash
python main.py
```

---

# Arborescence du projet

```
gestion_etudiants/
├── config/
│   └── connexion.py
    └── seed_data.py
├── models/
│   └── etudiant.py
    └── utilisateur.py
├── services/
│   └── etudiant_service.py
    └── export_service.py
    └── utilisateur_service.py
    └── statistiques.py
├── interface/
│   └── menu.py
     
├── utils/
│   └── auth.py
    └── validation.py
├── tests/
│   └── test_auth.py
    └── test_etudiant.py
├── main.py
├── .env
├── requirements.txt
└── README.md
```

---

# Remarque
Ce projet n’utilise pas Redis. Tous les fichiers liés à Redis présents dans l’environnement virtuel peuvent être ignorés parce que j’ai des problèmes avec redis c’est pourquoi je le fais avec MongoDB seulement.


---


# Auteur

- **Nom** : Madieume Diop
- **Email** : madieumediop99@gmail.com
- **Établissement** : Ecole 221