# coding: utf-8
import hashlib

from flask import *

import sql

app = Flask(__name__)
days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]


# Page d'accueil qui redirige vers la page de recherche ou page de login
@app.route('/')
def index():
    if 'mail' in session:
        return redirect(url_for("recherche"))

    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion'))


# Page de connexion
@app.route('/login', methods=['GET'])
def connexion():
    # Verif que l'utilisateur est connecté si connecté --> page de recherche sinon --> chargement template

    if 'mail' in session:

        return redirect(url_for('recherche',
                                info_msg="Vous êtes connecté, vous pouvez dès à présent accéder au"
                                         " service de tutorat."))

    else:

        hidemenu = True

        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')

        return render_template("connexion.html", **locals())


# Page de connexion
@app.route('/login', methods=['POST'])
def traitement_connexion():
    # Traitement du formulaire envoyé par l'utilisteur depuis la page login
    if 'mail' not in session:
        sql_obj = sql.MysqlObject()

        # obtenir les données entrées par l'utilisateur
        mail = request.form.get('mail')
        mdp = request.form.get('mdp')

        # chiffrer le mot de passe
        mdp_chiffre = hashlib.sha256(str(mdp).encode('utf-8')).hexdigest()

        # comparer les infos à celle de la base de données
        if mail in sql_obj.get_user_info('mail'):
            if sql_obj.get_crypt_mdp(mail)[0][0] == mdp_chiffre:

                # valider ou non  la connexion
                resp.set_cookie('session', 'mail')
                return redirect(url_for('recherche',
                                        info_msg="Vous êtes connecté, vous pouvez dès à présent accéder au service"
                                                 " de tutorat."))
            else:
                return redirect(url_for('connexion',
                                        info_msg="Erreur lors de la connexion, veuillez vérifier les informations"
                                                 " saisies puis réessayez."))
        else:
            return redirect(url_for('connexion',
                                    info_msg="Aucun compte ne correspond à l'adresse email renseignée."))
    else:
        return redirect(url_for('recherche',
                                info_msg="Vous êtes connecté, vous pouvez dès à présent accéder au"
                                         " service de tutorat."))


# Page d'inscription
@app.route('/register', methods=['GET'])
def inscription():
    if 'mail' not in session:
        sql_obj = sql.MysqlObject()
        if 'mail' not in sql_obj.get_user_info('mail'):

            sql_obj = sql.MysqlObject()
            # Propre à cette page
            hidemenu = True

            return render_template("inscription.html", classes=sql_obj.classes_liste(), **locals())
        else:
            return redirect(url_for('register', info_msg="Un compte est déjà associé à cette adresse email."))

    else:
        # Redirection vers la page d'accueil
        return redirect(url_for("recherche"))


@app.route('/register', methods=['POST'])
def traitement_inscription():
    sql_obj = sql.MysqlObject()

    # Chiffrement du mdp
    chaine_mot_de_passe = request.form.get('mdp')
    mot_de_passe_chiffre = hashlib.sha256(str(chaine_mot_de_passe).encode('utf-8')).hexdigest()

    nom = request.form.get('prenom') + '  ' + request.form.get('nom')
    # Envoi des infos à la base de données
    sql_obj.create_compte(nom, mot_de_passe_chiffre, request.form.get('mail'), request.form.get('classe'))
    return redirect(url_for("profil",
                            info_msg="Votre compte a bien été créé, vous pouvez dès à présent accéder à votre profil"
                                     " et au service d'offre/demande de Tutorat."))


# Mot de passe oublié
@app.route('/forgot', methods=['GET'])
def mdp_oublie():
    # Propre à cette page
    hidemenu = True

    return render_template("mdp_oublie.html", **locals())


# Traitement Mot de passe oublié
@app.route('/forgot', methods=['POST'])
def traitement_mdp_oublie():
    return redirect(url_for('connexion', info_msg="Un nouveau mot de passe a été envoyé à " + request.form['mail']))


# Page de Profil info utilisateur
@app.route('/profile/view')
def profil():
    if 'mail' in session:
        sql_obj = sql.MysqlObject()

        # TODO A FAIRE AVEC SESSION
        mail = "taotom63@gmail.com"
        admin_user = sql_obj.get_user_info(mail)[0][4]
        user = sql_obj.get_user_info(mail)[0][0]
        css_state = sql_obj.get_css(mail)

        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')

        return render_template("profil_u.html", infos=sql_obj.get_user_info(mail)[0], days=days, **locals())

    # Redirection si l'utilisateur n'est pas connecté
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))

# Page de Profil
@app.route('/profile/tutorials')
def profil2():
    if 'mail' in session:
        sql_obj = sql.MysqlObject()

        # TODO A FAIRE AVEC SESSION
        mail = "taotom63@gmail.com"
        admin_user = sql_obj.get_user_info(mail)[0][4]
        user = sql_obj.get_user_info(mail)[0][0]
        css_state = sql_obj.get_css(mail)

        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')

        return render_template("profil_p.html", offres_creees=sql_obj.get_user_offre(mail), tutorats_actifs=sql_obj.get_user_tutorats(mail), days=days, **locals())

    # Redirection si l'utilisateur n'est pas connecté
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page de modification du profil
@app.route('/profile/update', methods=['GET', 'POST'])
def profil_update():
    if 'mail' in session:
        sql_obj = sql.MysqlObject()

        # TODO A FAIRE AVEC SESSION
        mail = "taotom63@gmail.com"
        admin_user = sql_obj.get_user_info(mail)[0][4]
        user = sql_obj.get_user_info(mail)[0][0]
        css_state = sql_obj.get_css(mail)

        classes = sql_obj.classes_liste()

        if len(request.form) == 0:
            return render_template("profil_update.html", infos=sql_obj.get_user_info(mail)[0], **locals())
        else:
            if request.form.get('classe') in classes:

                sql_obj.modify_user_info(mail, request.form.get('classe'))
                return redirect(url_for("profil", info_msg="Votre profil a bien été modifié."))
            else:

                return render_template("error.html", message="Erreur - Veuillez vérifier les champs du formulaire",
                                       **locals())
    # Redirection si l'utilisateur n'est pas connecté
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page d'Administration offres en courts
@app.route('/admin/tutorials/progress', methods=['GET', 'POST'])
def admin_oc():
    sql_obj = sql.MysqlObject()

    # TODO A FAIRE AVEC SESSION
    mail = "taotom63@gmail.com"
    admin_user = sql_obj.get_user_info(mail)[0][4]
    user = sql_obj.get_user_info(mail)[0][0]
    css_state = sql_obj.get_css(mail)

    if admin_user:

        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')

        if request.form.get("user_search"):
            user_search = request.form.get("user_search")
            user_search = sql_obj.get_user_mail(user_search)
            return render_template("admin_t_p.html", tutorats_actifs=sql_obj.offres_liste_tri_admin(user_search),
                                   days=days, **locals())
        else:
            return render_template("admin_t_p.html", tutorats_actifs=sql_obj.offres_liste_validees(), days=days,
                                   **locals())

    else:
        abort(403)


# Page d'Administration offres à valider
@app.route('/admin/tutorials/validate')
def admin_ov():
    sql_obj = sql.MysqlObject()

    # TODO A FAIRE AVEC SESSION
    mail = "taotom63@gmail.com"
    admin_user = sql_obj.get_user_info(mail)[0][4]
    user = sql_obj.get_user_info(mail)[0][0]
    css_state = sql_obj.get_css(mail)

    if admin_user:

        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')

        return render_template("admin_t_v.html", offres_V=sql_obj.offres_liste_valider(), days=days, **locals())

    else:
        abort(403)


# Page d'Administration profile utilisateur
@app.route('/admin/users', methods=['GET', 'POST'])
def admin_u():
    sql_obj = sql.MysqlObject()

    # TODO A FAIRE AVEC SESSION
    mail = "taotom63@gmail.com"
    admin_user = sql_obj.get_user_info(mail)[0][4]
    user = sql_obj.get_user_info(mail)[0][0]
    css_state = sql_obj.get_css(mail)

    if admin_user:

        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')

        if request.form.get("user_search"):
            user_search = request.form.get("user_search")
            return render_template("admin_u.html", user_list=sql_obj.get_user_info_pseudo(user_search),
                                   tutorats_actifs=sql_obj.offres_liste_validees(), days=days, **locals())
        else:
            return render_template("admin_u.html", user_list=sql_obj.liste_user(),
                                   tutorats_actifs=sql_obj.offres_liste_validees(), days=days, **locals())

    else:
        abort(403)


# Page de recherche d'offres
@app.route('/search', methods=['GET', 'POST'])
def recherche():
    if 'mail' in session:
        sql_obj = sql.MysqlObject()

        # TODO A FAIRE AVEC SESSION
        mail = "taotom63@gmail.com"
        admin_user = sql_obj.get_user_info(mail)[0][4]
        user = sql_obj.get_user_info(mail)[0][0]
        css_state = sql_obj.get_css(mail)

        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')

        if request.form.get('precedent'):
            page = int(request.form.get('page')) - 1
        elif request.form.get('suivant'):
            page = int(request.form.get('page')) + 1
        else:
            page = 0

        # Variables locales utilisées dans les templates
        matieres = sql_obj.matieres_liste()
        filieres = sql_obj.filieres_liste()

        if request.form.get("option") and not request.form.get("option2"):
            # Formulaire de tri première étape

            option = request.form.get("option")
            return render_template("recherche.html", offres=sql_obj.offres_liste_tri(option, page, mail), days=days,
                                   **locals())

        elif request.form.get("option") and request.form.get("option2"):
            # Formulaire de tri deuxième étape

            option = request.form.get("option")
            option2 = request.form.get("option2")
            return render_template("recherche.html", offres=sql_obj.offres_liste_tri_2(option, option2, page, mail),
                                   days=days, **locals())

        else:
            # Aucune option de tri sélectionnée
            return render_template("recherche.html", offres=sql_obj.offres_liste(page, mail), days=days, **locals())

    # Redirection si l'utilisateur n'est pas connecté
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Affichage du formulaire de création d'une offre
@app.route('/create', methods=['GET'])
def creation():
    if 'mail' in session:
        sql_obj = sql.MysqlObject()

        # TODO A FAIRE AVEC SESSION
        mail = "taotom63@gmail.com"
        admin_user = sql_obj.get_user_info(mail)[0][4]
        user = sql_obj.get_user_info(mail)[0][0]
        css_state = sql_obj.get_css(mail)

        return render_template("creation.html", filieres=sql_obj.filieres_liste(), matieres=sql_obj.matieres_liste(),
                               days=days, **locals())

    # Redirection si l'utilisateur n'est pas connecté
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Traitement du formulaire + upload bdd
@app.route('/create', methods=['POST'])
def traitement_creation():
    # On ne traite pas la demande dans le doute ou l'élève n'a pas renseigné de créneau horaire
    process = False
    if 'mail' in session:
        sql_obj = sql.MysqlObject()

        # TODO A FAIRE AVEC SESSION
        mail = "taotom63@gmail.com"
        admin_user = sql_obj.get_user_info(mail)[0][4]
        user = sql_obj.get_user_info(mail)[0][0]
        css_state = sql_obj.get_css(mail)
        horaires = []

        for i in range(0, 12, 2):
            if request.form.get(sql.horaires_reference[i], None) != '' and request.form.get(
                    sql.horaires_reference[i + 1],
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
            filieres = sql_obj.filieres_liste()
            matieres = sql_obj.matieres_liste()

            if request.form.get("filiere") in filieres and request.form.get("matiere") in matieres:

                sql_obj.create_offre(mail, request.form.get('filiere'),
                                     request.form.get('matiere'),
                                     horaires)
                return redirect(url_for(
                    "recherche",
                    info_msg="Votre offre a bien été créée. Elle est actuellement en attente de validation."))

            else:
                return render_template("error.html", message="Erreur - Veuillez vérifier les champs du formulaire",
                                       **locals())
        else:
            # Erreur
            return render_template("error.html", message="Erreur - Veuillez renseigner au moins un horaire", **locals())

    # Redirection si l'utilisateur n'est pas connecté
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page d'enregistrement (s'enregistrer en tant que participant)
@app.route('/apply', methods=['POST'])
def enregistrement():
    if 'mail' in session:
        sql_obj = sql.MysqlObject()

        # TODO A FAIRE AVEC SESSION
        mail = "taotom63@gmail.com"
        admin_user = sql_obj.get_user_info(mail)[0][4]
        user = sql_obj.get_user_info(mail)[0][0]
        css_state = sql_obj.get_css(mail)

        result_code = sql_obj.add_participant(request.form.get("id"), mail)
        if result_code == 0:
            # Pas d'erreur
            return redirect(
                url_for("recherche", info_msg="Votre participation à ce tutorat a bien été prise en compte."))
        elif result_code == 1:
            # Erreur l'utilisateur participe déjà à l'offre
            return render_template("error.html", message="Erreur - Vous vous êtes déjà enregistré pour ce Tutorat",
                                   **locals())
        elif result_code == 2:
            # Erreur (cas très rare ou l'utilisateur accepte une offre qui est déjà pleine)
            return render_template("error.html", message="Erreur - Ce Tutorat est déjà plein", **locals())
        elif result_code == 3:
            # Erreur l'utilisateur veut participer à une offre qu'il a créée
            return render_template("error.html", message="Erreur - Vous êtes l'auteur de ce tutorat", **locals())
        elif result_code == 4:
            # Erreur l'utilisateur n'est pas dans la même classe que le premier participant
            return render_template("error.html",
                                   message="Erreur - Vous n'appartenez pas à la même classe que le premier participant",
                                   **locals())

    # Redirection si l'utilisateur n'est pas connecté
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Suppression de la participation d'un utilisateur à une offre
@app.route('/quit')
def quit_tutorat():
    if 'mail' in session:
        if request.args.get('id'):
            offre_id = request.args.get('id')
            sql_obj = sql.MysqlObject()

            # TODO A FAIRE AVEC SESSION
            mail = "taotom63@gmail.com"
            admin_user = sql_obj.get_user_info(mail)[0][4]
            user = sql_obj.get_user_info(mail)[0][0]
            css_state = sql_obj.get_css(mail)

            if sql_obj.delete_participant(offre_id, mail):
                return redirect(url_for("profil", info_msg="Votre retrait de ce Tutorat a bien été enregistré."))
            else:
                return render_template("error.html", message="Erreur - Vous ne participez pas à ce Tutorat", **locals())
        else:
            abort(403)

    # Redirection si l'utilisateur n'est pas connecté
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Suppression d'une offre
@app.route('/delete')
def delete():
    if request.args.get('id'):
        offre_id = request.args.get('id')
        sql_obj = sql.MysqlObject()
        # TODO vérifier que l'utilisateur a bien crée l'offre qu'il veut supprimer

        sql_obj.delete_offer(offre_id)
        return redirect(url_for("profil", info_msg="Votre offre a bien été supprimée."))
    else:
        abort(403)


# Suppression d'une offre (admin)
@app.route('/delete2')
def delete2():
    if request.args.get('id'):
        offre_id = request.args.get('id')
        sql_obj = sql.MysqlObject()
        # TODO vérifier que l'utilisateur est admin et s'il ne l'est pas le rediriger vers la page d'erreur

        sql_obj.delete_offer(offre_id)
        return redirect(url_for("admin_OC", info_msg="La suppression a bien été effectuée."))
    else:
        abort(403)


# Validation d'une offre (admin)
@app.route('/validate')
def validate():
    if request.args.get('id'):
        disponible = 1
        offre_id = request.args.get('id')
        sql_obj = sql.MysqlObject()
        # TODO vérifier que l'utilisateur est admin et s'il ne l'est pas le rediriger vers la page d'erreur

        sql_obj.validate_offer(offre_id, disponible)
        return redirect(url_for("admin_OV", info_msg="L'offre a bien été validée."))
    else:
        abort(403)


# Ban (admin)
@app.route('/ban')
def ban():
    # TODO vérifier que l'utilisateur est admin et s'il ne l'est pas le rediriger vers la page d'erreur
    if request.args.get('user_name'):
        user_name = request.args.get('user_name')
        sql_obj = sql.MysqlObject()

        sql_obj.ban(user_name)
        return redirect(url_for("admin_U", info_msg="Cet utilisateur a bien été banni."))
    else:
        abort(403)


# CSS
@app.route('/css')
def css():
    if 'mail' in session:
        sql_obj = sql.MysqlObject()
        # TODO A FAIRE AVEC SESSION
        mail = "taotom63@gmail.com"

        sql_obj.set_css(mail)

        # Redirection page d'avant
        return redirect(request.referrer)

    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Gestion de l'erreur 404
@app.errorhandler(404)
def not_found(error):
    # Propre à cette page
    hidemenu = True

    return render_template("error.html", message="Erreur 404 - Ressource non trouvée", **locals())


# Gestion de l'erreur 403
@app.errorhandler(403)
def forbidden(error):
    # Propre à cette page
    hidemenu = True

    return render_template("error.html", message="Erreur 403 - Accès Interdit", **locals())


# Gestion de l'erreur 405
@app.errorhandler(405)
def method_not_allowed(error):
    # Propre à cette page
    hidemenu = True

    return render_template("error.html", message="Erreur 405 - Méthode de requête non autorisée", **locals())


# Nécessaire pour faire fontionner les sessions
# (à garder secret pour que l'utilisateur ne puisse pas modifier les cookies)
# A modifier en Production
app.secret_key = '\x1c\xd7\x9c@\xe6\xdf\xb2\xab\xb1\x86\xa62\x85k_\x17\x93Q\xb7f\x9b\x10g\x0e'

# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
