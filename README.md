# Application Web LITReview

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](http://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-html.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/uses-css.svg)](https://forthebadge.com)

### Pré-requis

- Python 3.9 (Installer Python 3.9 depuis https://www.python.org/)
- Terminal
- Git
- Navigateur (Chrome, Firefox, Edge, Safari, etc...)


### Installation et exécution de l'application sans pipenv (avec venv et pip)

1. Clonez ce dépôt de code à l'aide de la commande `git clone https://github.com/seah78/P9.git`
2. Rendez-vous depuis un terminal dans le répertoire avec la commande `cd P9`
3. Créer un environnement virtuel pour le projet avec `python -m venv env` sous windows ou `python3 -m venv env` sous macos ou linux.
4. Activez l'environnement virtuel avec `env\Scripts\activate` sous windows ou `source env/bin/activate` sous macos ou linux.
5. Installez les dépendances du projet avec la commande `pip install -r requirements.txt`
6. Rendez-vous dans le répertoire avec la commande `cd src/`
6. Créer la base de données avec la commande `python manage.py migrate`
7. Démarrer le serveur avec `python manage.py runserver`

Les étapes 1 à 6 ne sont requises que pout l'installation initiale. Pour les lancements ultérieurs du serveur, il suffit d'exécuter l'étapes 7 à partir du répertoire P9/src.


## Démarrage

Depuis un navigateur, saisissez l'adresse http://127.0.0.1:8000/

## Résultat

La page d'inscription de naviagation s'ouvre dans le navigateur.

## Fabriqué avec

* Visual Studio Code

## Versions

Version actuelle : v1.0.0
Liste des versions : [Cliquer pour afficher](https://github.com/seah78/P9/tags)

## Auteurs

* ** Sébastien HERLANT ** _alias_ [@seah78](https://github.com/seah78)

## License

Ce projet est sous licence ``exemple: WTFTPL`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations


