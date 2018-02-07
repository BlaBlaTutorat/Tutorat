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


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
