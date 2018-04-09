# coding: utf-8
import hashlib

from flask import *

import sql

app = Flask(__name__)
days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]


# Page d'accueil qui redirige vers la page de recherche ou page de login
@app.route('/')
def index():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()

    # STATS
    nbr_users = sql_obj.stat_nombre()
    offres = sql_obj.stat_offres()
    # demandes = sql_obj.stat_demandes()
    # demandes_satisfaites = (sql_obj.stat_demandes() / sql_obj.stat_offres()) * 100

    return render_template("accueil.html", **locals())


# Page de connexion
@app.route('/login', methods=['GET'])
def connexion():
    # Verif que l'utilisateur est connecté si connecté --> page de recherche sinon --> chargement template
    sql_obj = sql.MysqlObject()
    if check_connexion():
        return redirect(url_for('recherche',
                                info_msg="Vous êtes connecté, vous pouvez dès à présent accéder au"
                                         " service de tutorat."))
    else:
        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')
        return render_template("authentification/connexion.html", **locals())


# Page de connexion
@app.route('/login', methods=['POST'])
def traitement_connexion():
    # Traitement du formulaire envoyé par l'utilisteur depuis la page login
    sql_obj = sql.MysqlObject()
    if not check_connexion():
        # obtenir les données entrées par l'utilisateur
        mail = request.form.get('mail')
        mdp = request.form.get('mdp')
        # chiffrer le mot de passe
        mdp_chiffre = hashlib.sha256(str(mdp).encode('utf-8')).hexdigest()
        # comparer les infos à celle de la base de données
        if sql_obj.mail_in_bdd(mail):
            if sql_obj.get_crypt_mdp(mail)[0][0] == mdp_chiffre:
                if not sql_obj.check_ban(mail):
                    session['mail'] = mail
                    return redirect(url_for('recherche',
                                            info_msg="Vous êtes connecté, vous pouvez dès à présent accéder au service"
                                                     " de tutorat."))
                else:
                    return redirect(url_for('connexion',
                                            info_msg="Vous êtes banni de cette platforme. Veuillez contacter un"
                                                     " documentaliste."))
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
    sql_obj = sql.MysqlObject()
    if not check_connexion():
        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')
        return render_template("authentification/inscription.html", classes=sql_obj.classes_liste(), **locals())
    else:
        # Redirection vers la page d'accueil
        return redirect(url_for("recherche"))


@app.route('/register', methods=['POST'])
def traitement_inscription():
    sql_obj = sql.MysqlObject()
    classes = sql_obj.classes_liste()
    if not check_connexion():
        if not sql_obj.mail_in_bdd(request.form['mail']):
            # Vérification que la classe est valide
            if request.form.get('classe') in classes:
                # Chiffrement du mdp
                chaine_mot_de_passe = request.form.get('mdp')
                mdp_confirm = request.form.get('mdp2')
                if chaine_mot_de_passe == mdp_confirm:
                    mot_de_passe_chiffre = hashlib.sha256(str(chaine_mot_de_passe).encode('utf-8')).hexdigest()
                    nom = request.form.get('prenom') + '  ' + request.form.get('nom')
                    # Envoi des infos à la base de données
                    sql_obj.create_compte(nom, mot_de_passe_chiffre, request.form.get('mail'),
                                          request.form.get('classe'))
                    return redirect(url_for("profil",
                                            info_msg="Votre compte a bien été créé,"
                                                     "vous pouvez dès à présent accéder à votre profil"
                                                     " et au service d'offre/demande de Tutorat."))
                else:
                    return render_template("authentification/inscription.html",
                                           info_msg='Les mots de passe ne correspondent pas.', **locals())
            else:
                return render_template("authentification/inscription.html",
                                       info_msg='Votre classe n\'est pas valide', **locals())
        else:
            return redirect(url_for('inscription',
                                    info_msg="Cette adresse email existe déjà"))
    else:
        # Redirection vers la page d'accueil
        return redirect(url_for("recherche"))


# Mot de passe oublié
@app.route('/forgot', methods=['GET'])
def mdp_oublie():
    return render_template("authentification/mdp_oublie.html", **locals())


# Traitement Mot de passe oublié
@app.route('/forgot', methods=['POST'])
def traitement_mdp_oublie():
    return redirect(url_for('connexion', info_msg="Un nouveau mot de passe a été envoyé à " + request.form['mail']))


# Page de Profil info utilisateur
@app.route('/profile/view')
def profil():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')
        return render_template("profil/profil_u.html", infos=sql_obj.get_user_info(mail)[0], days=days, **locals())
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page de Profil
@app.route('/profile/tutorials')
def profil_2():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')
        return render_template("profil/profil_t_p.html", offres_creees=sql_obj.get_user_offres(mail),
                               tutorats_actifs=sql_obj.get_user_tutorats(mail), days=days, **locals())
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page de supression Profil
@app.route('/profile/delete')
def profil_3():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        sql_obj.delete_account(mail)
        liste = sql_obj.get_user_tutorats(mail)
        for x in liste:
            sql_obj.delete_participant(x[0], mail)
        return redirect(url_for('connexion', info_msg="Votre compte a bien été supprimé. Au revoir."))
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page de profil d'un utilisateur
@app.route('/profile/view/<mail>')
def profil_4(mail):
    sql_obj = sql.MysqlObject()
    if check_connexion():
        if sql_obj.mail_in_bdd(mail):
            return render_template("profil/profil_visit.html", infos=sql_obj.get_user_info(mail)[0], **locals())
        else:
            return render_template("error.html", message="Erreur - Cet utilisateur n'existe pas",
                                   **locals())
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page de modification du profil
@app.route('/profile/update', methods=['GET', 'POST'])
def profil_update():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
        classes = sql_obj.classes_liste()
        if len(request.form) == 0:
            return render_template("profil/profil_update.html", infos=sql_obj.get_user_info(mail)[0], **locals())
        else:
            if request.form.get('classe') in classes:
                sql_obj.modify_user_info(mail, request.form.get('classe'))
                return redirect(url_for("profil", info_msg="Votre profil a bien été modifié."))
            else:
                return render_template("error.html", message="Erreur - Veuillez vérifier les champs du formulaire",
                                       **locals())
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page d'Administration offres en courts
@app.route('/admin/tutorials/progress', methods=['GET', 'POST'])
def admin_oc():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
        if admin_user:
            if request.args.get('info_msg'):
                info_msg = request.args.get('info_msg')
            if request.form.get("user_search"):
                user_search = request.form.get("user_search")
                user_search = sql_obj.get_user_info_pseudo(user_search)
                if len(user_search) == 1:
                    # Un utilisateur a été trouvée
                    return render_template("admin/admin_t_p.html",
                                           tutorats_actifs=sql_obj.offres_liste_tri_admin(user_search[0][2]),
                                           days=days, **locals())
                else:
                    # Pas d'utilisateur trouvé donc liste vide
                    return render_template("admin/admin_t_p.html", tutorats_actifs=[], days=days,
                                           **locals())
            else:
                return render_template("admin/admin_t_p.html", tutorats_actifs=sql_obj.offres_liste_validees(),
                                       days=days, **locals())
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez vous avant de continuer.'))


# Page d'Administration offres à valider
@app.route('/admin/tutorials/validate')
def admin_ov():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
        if admin_user:
            if request.args.get('info_msg'):
                info_msg = request.args.get('info_msg')
            if request.args.get('reset_msg'):
                reset_msg = request.args.get('reset_msg')
            return render_template("admin/admin_t_v.html", offres_V=sql_obj.offres_liste_valider(), days=days,
                                   **locals())
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez vous avant de continuer.'))


# Page d'Administration profile utilisateur
@app.route('/admin/users', methods=['GET', 'POST'])
def admin_u():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
        if admin_user:
            if request.args.get('info_msg'):
                info_msg = request.args.get('info_msg')
            if request.form.get("user_search"):
                user_search = request.form.get("user_search")
                return render_template("admin/admin_u.html", user_list=sql_obj.get_user_info_pseudo(user_search),
                                       tutorats_actifs=sql_obj.offres_liste_validees(), days=days, **locals())
            else:
                return render_template("admin/admin_u.html", user_list=sql_obj.liste_user(),
                                       tutorats_actifs=sql_obj.offres_liste_validees(), days=days, **locals())
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez vous avant de continuer.'))


# Page de recherche d'offres
@app.route('/search', methods=['GET', 'POST'])
def recherche():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
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

    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Affichage du formulaire de création d'une offre
@app.route('/create', methods=['GET'])
def creation():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
        return render_template("creation.html", filieres=sql_obj.filieres_liste(), matieres=sql_obj.matieres_liste(),
                               days=days, **locals())
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Traitement du formulaire + upload bdd
@app.route('/create', methods=['POST'])
def traitement_creation():
    # On ne traite pas la demande dans le doute ou l'élève n'a pas renseigné de créneau horaire
    process = False
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
        horaires = []
        for i in range(0, 12, 2):
            debut = sql.get_horaire(i)
            fin = sql.get_horaire(i+1)

            if request.form.get(debut, None) != '' and request.form.get(
                    fin, None) != '':
                # L'élève a renseigné au moins un créneau horaire
                process = True
                horaires.append(request.form.get(debut))
                horaires.append(request.form.get(fin))
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
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page d'enregistrement (s'enregistrer en tant que participant)
@app.route('/apply', methods=['POST'])
def enregistrement():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        result_code = sql_obj.add_participant(request.form.get("id"), mail)
        if result_code == 0:
            # Pas d'erreur
            return redirect(
                url_for("recherche", info_msg="Votre participation à ce tutorat a bien été prise en compte."))
        elif result_code == 1:
            # Erreur l'utilisateur participe déjà à l'offre
            return redirect(url_for("recherche", info_msg="Vous vous êtes déjà enregistré pour ce Tutorat"))
        elif result_code == 2:
            # Erreur (cas très rare ou l'utilisateur accepte une offre qui est déjà pleine)
            return redirect(url_for("recherche", info_msg="Ce Tutorat est déjà plein"))
        elif result_code == 3:
            # Erreur l'utilisateur veut participer à une offre qu'il a créée
            return redirect(url_for("recherche", info_msg="Vous êtes l'auteur de ce tutorat"))
        elif result_code == 4:
            # Erreur l'utilisateur n'est pas dans la même classe que le premier participant
            return redirect(
                url_for("recherche", info_msg="Vous n'appartenez pas à la même classe que le premier participant"))
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Suppression de la participation d'un utilisateur à une offre
@app.route('/quit')
def quit_tutorat():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        if request.args.get('id'):
            offre_id = request.args.get('id')
            mail = session['mail']
            if sql_obj.delete_participant(offre_id, mail):
                return redirect(url_for("profil", info_msg="Votre retrait de ce Tutorat a bien été enregistré."))
            else:
                return redirect(url_for("profil", info_msg="Vous ne participez pas à ce Tutorat"))
        else:
            abort(403)
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Suppression d'une offre
@app.route('/delete')
def delete():
    if check_connexion():
        mail = session['mail']
        if request.args.get('id'):
            sql_obj = sql.MysqlObject()
            offre_id = request.args.get('id')
            offre = sql_obj.get_offre(offre_id)
            # Vérification qu'une seule offre avec cet id existe
            if len(offre) == 1:
                # Vérification que l'auteur est celui qui demande la suppression
                if mail == offre[0][1]:
                    sql_obj.delete_offer(offre_id)
                    return redirect(url_for("profil", info_msg="Votre offre a bien été supprimée."))
                else:
                    abort(403)
            else:
                abort(403)
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Suppression d'une offre (admin)
@app.route('/delete2')
def delete2():
    if check_connexion():
        admin_user = check_admin()
        if admin_user:
            if request.args.get('id'):
                offre_id = request.args.get('id')
                sql_obj = sql.MysqlObject()
                sql_obj.delete_offer(offre_id)
                return redirect(url_for("admin_oc", info_msg="La suppression a bien été effectuée."))
            else:
                abort(403)
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Validation d'une offre (admin)
@app.route('/validate')
def validate():
    if check_connexion():
        admin_user = check_admin()
        if admin_user:
            if request.args.get('id'):
                disponible = 1
                offre_id = request.args.get('id')
                sql_obj = sql.MysqlObject()
                sql_obj.validate_offer(offre_id, disponible)
                return redirect(url_for("admin_ov", info_msg="L'offre a bien été validée."))
            else:
                abort(403)
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Ban (admin)
@app.route('/ban')
def ban():
    if check_connexion():
        admin_user = check_admin()
        if admin_user:
            if request.args.get('mail'):
                mail = request.args.get('mail')
                sql_obj = sql.MysqlObject()
                sql_obj.ban(mail)
                return redirect(url_for("admin_u", info_msg="Le statut de cet utilisateur a bien été mis à jour."))
            else:
                abort(403)
        else:
            abort(403)
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Promouvoir (admin)
@app.route('/promote')
def promote():
    if check_connexion():
        admin_user = check_admin()
        if admin_user:
            if request.args.get('mail'):
                mail = request.args.get('mail')
                sql_obj = sql.MysqlObject()
                sql_obj.promote(mail)
                return redirect(url_for("admin_u", info_msg="Le statut de cet utilisateur a bien été mis à jour."))
            else:
                abort(403)
        else:
            abort(403)
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# deconnexion
@app.route('/disconnect')
def deconnexion():
    if check_connexion():
        session.pop('mail', None)
        return redirect(url_for("connexion", info_msg='Vous avez bien été déconnecté.'))
    else:
        return redirect(url_for("connexion"))


# Remise à 0
@app.route('/reset')
def reset():
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        if admin_user == 1:
            sql_obj.reset()
            info_msg = 'Le site BlaBla Tutorat a bien été remis à zéro.'
            return redirect(url_for('admin_ov', offres_V=sql_obj.offres_liste_valider(), days=days, **locals()))
        else:
            abort(403)
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Gestion de l'erreur 404
@app.errorhandler(404)
def not_found(error):
    return render_template("error.html", message="Erreur 404 - Ressource non trouvée", **locals())


# Gestion de l'erreur 403
@app.errorhandler(403)
def forbidden(error):
    return render_template("error.html", message="Erreur 403 - Accès Interdit", **locals())


# Gestion de l'erreur 405
@app.errorhandler(405)
def method_not_allowed(error):
    return render_template("error.html", message="Erreur 405 - Méthode de requête non autorisée", **locals())


# Vérification connexion
def check_connexion():
    # Verification mail non nul
    if 'mail' in session:
        sql_obj = sql.MysqlObject()
        mail = session['mail']
        # Vérification mail existe
        if sql_obj.mail_in_bdd(mail):
            if sql_obj.check_ban(mail):
                return False
            else:
                return True
        else:
            return False
    else:
        return False


# Vérification admin
def check_admin():
    if 'mail' in session:
        sql_obj = sql.MysqlObject()
        mail = session['mail']
        # Vérification mail existe
        if sql_obj.mail_in_bdd(mail):
            if sql_obj.get_user_info(mail)[0][3] == "ADMIN":
                return True
            else:
                return False
        else:
            return False
    else:
        return False


# Possibilité d'appeler la fonction check_connexion() depuis un template html
app.jinja_env.globals.update(check_connexion=check_connexion)

# Nécessaire pour faire fontionner les sessions
# (à garder secret pour que l'utilisateur ne puisse pas modifier les cookies)
# A modifier en Production
app.secret_key = '\x1c\xd7\x9c@\xe6\xdf\xb2\xab\xb1\x86\xa62\x85k_\x17\x93Q\xb7f\x9b\x10g\x0e'
# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
