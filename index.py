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
    return render_template("inscription.html", admin=False, hidemenu=True, niveaux=sql_obj.niveaux_liste())


# Profil
@app.route('/profil')
def profil():
    return "Mon profil"


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
    created = False
    if request.args.get('created'):
        created = True

    if len(request.form) > 0:
        return render_template("recherche.html", admin=False, user="Moi",
                               offres=sql_obj.offres_liste_tri(request.form.get("option")),
                               created=created, option=request.form.get("option"))
    else:
        return render_template("recherche.html", admin=False, user="Moi", offres=sql_obj.offres_liste(),
                               created=created)


# Page d'enregistrement (s'enregistrer en tant que participant)
@app.route('/apply', methods=['POST'])
def enregistrement():
    return "Processing id: " + request.form.get("id")


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
            horaires.append(0)
            horaires.append(0)

    if process:
        sql_obj = sql.MysqlObject()
        sql_obj.create_offre(request.form.get('auteur'), request.form.get('niveau'), request.form.get('matiere'),
                             horaires)
        return redirect(url_for("recherche", created=True))
    else:
        return render_template("error.html", message="Vous n'avez pas remplis tous les champs requis (horaires)")


# Gestion des erreurs 404
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html", message="Erreur 404: Ressource non trouvée")


# Gestion des erreurs 403
@app.errorhandler(403)
def forbidden(error):
    return render_template("error.html", message="Erreur 403: Accès Interdit")


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
