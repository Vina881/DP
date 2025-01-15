# Système de Gestion de Bibliothèque en Ligne - LibraryGo 

## PROJET 1 - Membres 👥

```bash
-RAMANANTOANINA Anja Malina n°23
-RAKOTOTSIFA Alexandro Tolotra n°19
-RAHARITSIFA Vina Maharotoky n°15
-RAMAMONJISOA Antsa Ny Aro Tanya N°22 
```

## Fonctionnalités ✨

```bash
-🔐 Authentification (Membre, Bibliothécaire, Administrateur)
-📚 Gestion des Livres
-🎫 Système de Reservation
-📑 Gestion des Catégories
-📊 Génération de Rapports
-🔔 Notifications en Temps Réel
```

## Technologies Utilisées 🛠️

```bash
-Python 3.8+
-Flask
-MySQL
-HTML/CSS/JavaScript
```


## Installation 🚀

### 1. Cloner le dépôt

```bash
$ git clone [git@github.com:Vina881/DP.git]
```

### 2. Créer un environnement virtuel
```bash
$ python -m venv venv
$ source venv/bin/activate  # Linux/Mac
$ venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances
```bash
$ pip install -r requirements.txt
```

### 4. Configurer la Base de Données
```bash
$ mysql -u root -p librarygo < db/schema.sql
```

### 5. Définir les variables d'environnement
```bash
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

### 6. Lancer l'application
```bash
$ flask run
```

## Accès par Défaut 🔑
```bash
$ Connexion Admin:
$ Email: admin@librarygo.com
$ Mot de passe: admin123

$ Connexion Bibliothécaire:
$ Email: librarian@librarygo.com
$ Mot de passe: librarian123
```
## Structure du Projet 📁

```bash
$ librarygo/
$ ├── app.py                  # Point d'entrée de l'application
$ ├── routes/                 # Définitions des routes URL
$ ├── Controllers/            # Logique métier
$ ├── Models/                 # Modèles de base de données
$ ├── App/                    # Implémentation des patterns
$ └── templates/              # Templates HTML
```

## Design Patterns Implémentés 🌐

```bash
-MVC
-Composite Pattern
-Singleton Pattern
-Factory Pattern
-Observer Pattern
-Strategy Pattern
-Command Pattern
-Decorator Pattern
-Template Method Pattern
-State Pattern
-Mediator Pattern
-Chain of Responsibility
-Composite Pattern
-Visitor Pattern
-Builder Pattern
```
