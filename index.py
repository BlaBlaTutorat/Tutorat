from flask import *

app = Flask(__name__)


# Page d'accueil
@app.route('/')
def index():
    return "Accueil"


# Page de connection
@app.route('/login')
def connection():
    return render_template("connexion.html")


# Page d'inscription
@app.route('/register')
def inscription():
    return render_template("inscription.html")


# Profil
@app.route('/profil')
def profil():
    return "Mon profil"


# Mot de passe oublié
@app.route('/forgot')
def mdp_oublie():
    return render_template("mdp_oublie.html")


# Page de validation
@app.route('/validate')
def validation():
    return render_template("validation.html")


# Page de recherche d'offres
@app.route('/search')
def recherche():
    return render_template("recherche.html")


# Affichage du formulaire de création d'une offre
@app.route('/create', methods=['GET'])
def creation():
    return render_template("creation.html")


# Traitement du formulaire + upload bdd
@app.route('/create', methods=['POST'])
def traitement_creation():
    return "Processing"


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
