from flask import Flask

app = Flask(__name__)


# Page d'accueil
@app.route('/')
def index():
    return "Accueil"


# Page de connection
@app.route('/login')
def connection():
    return "connection"


# Page d'inscription
@app.route('/register')
def inscription():
    return "inscription"


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
