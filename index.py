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
@app.route('/search')
def recherche():
    sql_obj = sql.MysqlObject()
    return render_template("recherche.html", admin=False, user="Moi", offres=sql_obj.offres_liste())


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
    return "Processing auteur: " + request.form.get('auteur') + " niveau: " + request.form.get(
        'niveau') + " matière: " + request.form.get('matiere')


# Gestion des erreurs 404
@app.errorhandler(404)
def not_found(error):
    return "Erreur 404: Ressource non trouvée"


# Gestion des erreurs 403
@app.errorhandler(403)
def forbidden(error):
    return "Erreur 403: Accès Interdit"


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
