## [Projet d'ISN de tutorat](http://info.blaisepascal.fr/blabla-tutorat)

#### Répartition des tâches:
 - Tao : CSS + Header + Footer + Administration
 - Marko : Inscription + Connexion
 - Antoine : Recherche + Création et participation aux Tutorats + Profil

#### Langages:
- Python
- SQL
- HTML
- CSS

#### Mise en page:
- 1 Page de Connexion
- 1 Page d'Inscription
- 1 Page de Recherche
- 1 Page pour Poster des offres
- 1 Page de Gestion Administrateur
- 1 Page de Profil
    
#### Tables:
- Utilisateurs:
    - Nom (PRIMARY)
    - Mot de passe
    - Email
    - Classe
    - Ban (boolean)
    - Admin (boolean)
    - Css (boolean)

- Offres:
    - Id (PRIMARY)
    - Matière
    - Auteur
    - Filiere
    - Date de création
    - Disponible (boolean)
    - Participant
    - Participant2
    - Créneaux horaires

- Matières:
    - PRONOTE

- Classes:
    - PRONOTE
    
- Filieres
    - Nom(PRIMARY)