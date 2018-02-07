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


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
