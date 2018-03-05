Projet d'isn de tutorat

Répartition des taches:
 - Tao : CSS + header + footer + administration
 - Marko : Inscription + Connexion
 - Antoine : Recherche + Postage et acceptation des offres + profil

Langages:
- Python
- SQL
- HTML
- CSS

Mise en page:
- 1 Page de connexion
- 1 Page d'inscription
- 1 Page Recherche
- 1 Page Poster des offres
- 1 Page Gestion administrateur
    
Tables:

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
    - Classe
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