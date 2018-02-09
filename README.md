Projet d'isn de tutorat

Langages:
- Python
- SQL
- HTML
- CSS

Mise en page:
- 1 Page d'accueil
- 1 Page de connexion
- 1 Page d'inscription
- 1 Page Recherche / Poster des offres
    
Tables:

- Utilisateurs:
    - Login(PRIMARY)
    - Mot de passe
    - Email
    - Niveau
    - Signalement (3 = Ban)
    - Admin (boolean)

- Offres:
    - Matière
    - Auteur
    - Créneaux horaires
    - Niveau
    - id (PRIMARY)
    - Disponible (boolean)
    - Participant(s) 2MAX

- Matières:
    - Nom(PRIMARY)

- Classes:
    - id (PRIMARY)
    - niveau
    - specialite
    - numero

- Specialites:
    - Nom (PRIMARY)
    
 - Niveaux:
    - ID (PRIMARY)
    - Nom