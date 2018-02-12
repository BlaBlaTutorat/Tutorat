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
    - Filière
    - Ban (boolean)
    - Admin (boolean)

- Offres:
    - Matière
    - Auteur
    - Niveau
    - Filière
    - id (PRIMARY)
    - Date de création
    - Disponible (boolean)
    - Participant
    - Participant2
    - Créneaux horaires

- Matières:
    - Nom(PRIMARY)

- Classes:
    - id (PRIMARY)
    - niveau
    - specialite
    - numero

- Filières:
    - ID (PRIMARY)
    - Nom
    
 - Niveaux:
    - ID (PRIMARY)
    - Nom