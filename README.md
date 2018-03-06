## [Projet d'ISN de tutorat](http://info.blaisepascal.fr/blabla-tutorat)

#### Répartition des tâches:
 - Tao :
      - Thème claire (CSS)
      - Thème foncé (CSS)
      - Header (HTML)
      - Footer (HTML)
      - Page Administration (HTML, SQL, Python)
      
 - Marko : 
      - Page Inscription (HTML, SQL, Python)
      - Page Connexion (HTML, SQL, Python)
      - Gestion utilisateurs : savoir qui est connecté (?)
      
 - Antoine : 
      - Page Recherche (HTML, SQL, Python)
      - Page Création (HTML, SQL, Python)
      - Page Profil (HTML, SQL, Python)
      - Page MAJ Profil (HTML, SQL, Python)
      - Gestion tutorats : qui y participe (SQL)


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
