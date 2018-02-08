from flask import *

app = Flask(__name__)


# Page d'accueil
@app.route('/')
def index():
    return "Accueil"


# Page de connection
@app.route('/login')
def connection():
    return render_template("connexion.html", admin=False)


# Page d'inscription
@app.route('/register')
def inscription():
    return render_template("inscription.html", admin=False)


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
    return render_template("recherche.html", admin=False)


# Affichage du formulaire de création d'une offre
@app.route('/create', methods=['GET'])
def creation():
    return render_template("creation.html", admin=False)


# Traitement du formulaire + upload bdd
@app.route('/create', methods=['POST'])
def traitement_creation():
    return "Processing"


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
