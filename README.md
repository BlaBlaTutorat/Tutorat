## [Projet d'ISN de tutorat](http://info.blaisepascal.fr/blabla-tutorat)

#### Langages:
- Python
- SQL
- HTML
- CSS
- JS
    
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
    - Horaires
    
- Demandes:
    - Id (PRIMARY)
    - Matière
    - Auteur
    - Classe
    - Date de création
    - Disponible (boolean)
    - Tuteur
    - Horaires

- Matières:
    - LIBELLE (PRONOTE)

- Classes:
    - NOM (PRONOTE)
    
- Filieres
    - Nom(PRIMARY)
    - Classement
