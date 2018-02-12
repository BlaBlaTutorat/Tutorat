from flask import *
import sql

app = Flask(__name__)


# Page d'accueil
@app.route('/')
def index():
    return "Accueil"


# Page de connection
@app.route('/login')
def connection():
    return render_template("connexion.html", admin=False, hidemenu=True)


# Page d'inscription
@app.route('/register')
def inscription():
    sql_obj = sql.MysqlObject()
    return render_template("inscription.html", admin=False, hidemenu=True, niveaux=sql_obj.niveaux_liste(),
                           filieres=sql_obj.filieres_liste())


# Profil
@app.route('/profil')
def profil():
    sql_obj = sql.MysqlObject()
    return render_template("profil.html", infos=sql_obj.get_user_info("Jean Kévin"))


# Administration
@app.route('/admin')
def admin():
    return "Administration"


# Mot de passe oublié
@app.route('/forgot')
def mdp_oublie():
    return render_template("mdp_oublie.html", admin=False)


# Page de validation
@app.route('/validate')
def validation():
    return render_template("validation.html", admin=False)


# Page de recherche d'offres
@app.route('/search', methods=['GET', 'POST'])
def recherche():
    sql_obj = sql.MysqlObject()
    info_msg = None
    if request.args.get('info_msg'):
        info_msg = request.args.get('info_msg')

    if len(request.form) == 1:
        # Formulaire de tri première étape
        return render_template("recherche.html", admin=False, user="Moi",
                               offres=sql_obj.offres_liste_tri(request.form.get("option")),
                               info_msg=info_msg, option=request.form.get("option"), matieres=sql_obj.matieres_liste(),
                               niveaux=sql_obj.niveaux_liste())
    elif len(request.form) > 1:
        # Formulaire de tri deuxième étape
        return render_template("recherche.html", admin=False, user="Moi",
                               offres=sql_obj.offres_liste_tri_2(request.form.get("option"),
                                                                 request.form.get("option2")),
                               info_msg=info_msg, option=request.form.get("option"),
                               option2=request.form.get("option2"),
                               matieres=sql_obj.matieres_liste(),
                               niveaux=sql_obj.niveaux_liste())
    else:
        # Pas de formulaire de tri
        return render_template("recherche.html", admin=False, user="Moi", offres=sql_obj.offres_liste(),
                               info_msg=info_msg)


# Page d'enregistrement (s'enregistrer en tant que participant)
@app.route('/apply', methods=['POST'])
def enregistrement():
    participant = "Moi"
    sql_obj = sql.MysqlObject()
    result_code = sql_obj.add_participant(request.form.get("id"), participant)
    if result_code == 0:
        # Pas d'erreur
        return redirect(url_for("recherche", info_msg="Votre participation à ce tutorat a bien été prise en compte"))
    elif result_code == 1:
        # Erreur l'utilisateur participe déjà à l'offre
        return render_template("error.html", message="Vous vous êtes déjà enregistrés pour ce Tutorat.")
    elif result_code == 2:
        # Erreur (cas très rare ou l'utilisateur accepte une offre qui est deja pleine)
        return render_template("error.html", message="Ce Tutorat est déjà plein.")


# Affichage du formulaire de création d'une offre
@app.route('/create', methods=['GET'])
def creation():
    sql_obj = sql.MysqlObject()
    return render_template("creation.html", admin=False, user="Moi", niveaux=sql_obj.niveaux_liste(),
                           matieres=sql_obj.matieres_liste())


# Traitement du formulaire + upload bdd
@app.route('/create', methods=['POST'])
def traitement_creation():
    # On ne triate pas la demande dans le doute ou l'élève n'a pas renseigné de créneau horaire
    process = False
    horaires = []

    for i in range(0, 12, 2):
        if request.form.get(sql.horaires_reference[i], None) != '' and request.form.get(sql.horaires_reference[i + 1],
                                                                                        None) != '':
            # L'élève a renseigné au moins un créneau horaire
            process = True
            horaires.append(request.form.get(sql.horaires_reference[i]))
            horaires.append(request.form.get(sql.horaires_reference[i + 1]))
        else:
            # Créneau horaire vide, on remplit avec des zéros
            horaires.append(0)
            horaires.append(0)

    if process:
        # Création
        sql_obj = sql.MysqlObject()
        sql_obj.create_offre(request.form.get('auteur'), request.form.get('niveau'), request.form.get('matiere'),
                             horaires)
        return redirect(url_for("recherche",
                                info_msg="Votre offre a bien été créée. Elle est actuellement en attente de validation."))
    else:
        # Erreur
        return render_template("error.html", message="Vous n'avez pas remplis tous les champs requis (horaires)")


# Gestion de l'erreur 404
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html", message="Erreur 404: Ressource non trouvée.")


# Gestion de l'erreur 403
@app.errorhandler(403)
def forbidden(error):
    return render_template("error.html", message="Erreur 403: Accès Interdit.")


# Gestion de l'erreur 405
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("error.html", message="Erreur 405: Méthode de requête non autorisée.")


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
