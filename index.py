from flask import *

import sql

app = Flask(__name__)
days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]


# Page d'accueil qui redirige vers la page de recherche si l'utilisateur est connecté
@app.route('/')
def index():
    return redirect(url_for("recherche"))


# Page de connection
@app.route('/login')
def connection():
    # Propre à cette page
    hidemenu = True

    admin_user = True
    info_msg = None
    if request.args.get('info_msg'):
        info_msg = request.args.get('info_msg')
    return render_template("connexion.html", **locals())


# Page d'inscription
@app.route('/register')
def inscription():
    sql_obj = sql.MysqlObject()
    # Propre à cette page
    hidemenu = True

    admin_user = True

    return render_template("inscription.html", **locals(), niveaux=sql_obj.niveaux_liste(),
                           filieres=sql_obj.filieres_liste())


# Page de Profil
@app.route('/profil')
def profil():
    sql_obj = sql.MysqlObject()
    admin_user = True
    user_name = "Tao Blancheton"
    return render_template("profil.html", **locals(), infos=sql_obj.get_user_info(user_name),
                           offres=sql_obj.get_user_offre(user_name), days=days)


# Page d'Administration
@app.route('/admin')
def admin():
    return "Administration"


# Mot de passe oublié
@app.route('/forgot')
def mdp_oublie():
    # Propre à cette page
    hidemenu = True

    admin_user = True
    return render_template("mdp_oublie.html", **locals())


# Page de recherche d'offres
@app.route('/search', methods=['GET', 'POST'])
def recherche():
    sql_obj = sql.MysqlObject()
    admin_user = True
    info_msg = None
    if request.args.get('info_msg'):
        info_msg = request.args.get('info_msg')

    if request.form.get('precedent'):
        page = int(request.form.get('page')) - 1
    elif request.form.get('suivant'):
        page = int(request.form.get('page')) + 1
    else:
        page = 0

    if request.form.get("option") and not request.form.get("option2"):
        # Formulaire de tri première étape
        option = request.form.get("option")
        return render_template("recherche.html", **locals(), offres=sql_obj.offres_liste_tri(option, page),
                               matieres=sql_obj.matieres_liste(), niveaux=sql_obj.niveaux_liste(),
                               filieres=sql_obj.filieres_liste(), days=days)
    elif request.form.get("option") and request.form.get("option2"):
        # Formulaire de tri deuxième étape
        option = request.form.get("option")
        option2 = request.form.get("option2")
        return render_template("recherche.html",
                               offres=sql_obj.offres_liste_tri_2(option, option2, page), **locals(), days=days,
                               matieres=sql_obj.matieres_liste(), niveaux=sql_obj.niveaux_liste(),
                               filieres=sql_obj.filieres_liste())
    else:
        # Pas de formulaire de tri
        return render_template("recherche.html", **locals(), offres=sql_obj.offres_liste(page), days=days)


# Page d'enregistrement (s'enregistrer en tant que participant)
@app.route('/apply', methods=['POST'])
def enregistrement():
    participant = "Tao Blancheton"
    sql_obj = sql.MysqlObject()
    result_code = sql_obj.add_participant(request.form.get("id"), participant)
    if result_code == 0:
        # Pas d'erreur
        return redirect(url_for("recherche", info_msg="Votre participation à ce tutorat a bien été prise en compte."))
    elif result_code == 1:
        # Erreur l'utilisateur participe déjà à l'offre
        return render_template("error.html", message="Erreur - Vous vous êtes déjà enregistrés pour ce Tutorat")
    elif result_code == 2:
        # Erreur (cas très rare ou l'utilisateur accepte une offre qui est deja pleine)
        return render_template("error.html", message="Erreur - Ce Tutorat est déjà plein")


# Affichage du formulaire de création d'une offre
@app.route('/create', methods=['GET'])
def creation():
    sql_obj = sql.MysqlObject()
    admin_user = True
    user = "Tao Blancheton"
    return render_template("creation.html", **locals(), niveaux=sql_obj.niveaux_liste(),
                           matieres=sql_obj.matieres_liste(), filieres=sql_obj.filieres_liste(), days=days)


# Traitement du formulaire + upload bdd
@app.route('/create', methods=['POST'])
def traitement_creation():
    # On ne traite pas la demande dans le doute ou l'élève n'a pas renseigné de créneau horaire
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
        sql_obj.create_offre(request.form.get('auteur'), request.form.get('niveau'), request.form.get('filiere'),
                             request.form.get('matiere'), horaires)
        return redirect(url_for(
            "recherche", info_msg="Votre offre a bien été créée. Elle est actuellement en attente de validation."))
    else:
        # Erreur
        return render_template("error.html", message="Vous n'avez pas remplis tous les champs requis (horaires)")


# Suppression d'un offre
@app.route('/delete')
def delete():
    if request.args.get('id'):
        offre_id = request.args.get('id')
        sql_obj = sql.MysqlObject()
        # TODO A OPTIMISER AVEC L'AUTHENTIFICATION
        user = "Tao Blancheton"

        sql_obj.delete_offer(offre_id)
        return redirect(url_for("recherche", info_msg="Votre offre a bien été supprimée."))
    else:
        abort(403)


# Gestion de l'erreur 404
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html", message="Erreur 404 - Ressource non trouvée")


# Gestion de l'erreur 403
@app.errorhandler(403)
def forbidden(error):
    return render_template("error.html", message="Erreur 403 - Accès Interdit")


# Gestion de l'erreur 405
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("error.html", message="Erreur 405 - Méthode de requête non autorisée")


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
