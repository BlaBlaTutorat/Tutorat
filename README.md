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
    - Nom
    - Mot de passe
    - Email (PRIMARY)
    - Niveau
    - Filière
    - Ban (boolean)
    - Admin (boolean)
    - Css (boolean)

- Offres:
    - Id (PRIMARY)
    - Matière
    - Auteur
    - Niveau
    - Filière
    - Date de création
    - Disponible (boolean)
    - Participant
    - Participant2
    - Créneaux horaires

- Matières:
    - Nom (PRIMARY)

- Classes:
    - Id (PRIMARY)
    - Niveau
    - Spécialité
    - Numéro

- Filières:
    - ID (PRIMARY)
    - Nom
    
 - Niveaux:
    - ID (PRIMARY)
    - Nom
