# coding: utf-8
import hashlib
import random
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import *

import config  # config1 en production
import sql

app = Flask(__name__)
days = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]


# Page d'accueil qui redirige vers la page de recherche ou page de login
@app.route('/')
def index():
    """Page d'accueil qui redirige vers la page de recherche ou page de login"""
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()

    # STATS
    nbr_users = sql_obj.stat_nombre()
    offres = sql_obj.stat_offres()
    demandes = sql_obj.stat_demandes()

    return render_template("accueil.html", **locals())


# Page de connexion
@app.route('/login', methods=['GET'])
def connexion():
    """Page de connexion"""
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
    """Compare les données rentré par l'utilisateur à celles de la BDD et nous connect si les données correspondent"""
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
    """Page d'inscription"""
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
    """Envoie les données rentré par l'utilisateur à la BDD pour l'inscrire"""
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
                    nom = request.form.get('prenom') + ' ' + request.form.get('nom')
                    # Envoi des infos à la base de données
                    sql_obj.create_compte(nom, mot_de_passe_chiffre, request.form.get('mail'),
                                          request.form.get('classe'))
                    return redirect(url_for("connexion",
                                            info_msg="Votre compte a bien été créé, "
                                                     "vous pouvez dès à présent vous connecter"))
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
    """Page de mot de passe oublié"""
    if request.args.get('info_msg'):
        info_msg = request.args.get('info_msg')
    # Vérification configuration complète
    if config.email != "" and config.email_password != "":
        return render_template("authentification/mdp_oublie.html", **locals())
    else:
        return redirect(url_for('connexion', info_msg="Veuillez vous adresser directement aux documentalistes."))


# Traitement Mot de passe oublié
@app.route('/forgot', methods=['POST'])
def traitement_mdp_oublie():
    """Créé un nouveau mot de passe aléatoirement et l'envoie par mail à l'utilisateur"""
    sql_obj = sql.MysqlObject()
    if not check_connexion():
        if sql_obj.mail_in_bdd(request.form['mail']):
            # Génération nouveau mot de passe
            element = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-*/~$%&.:?!"
            passwd = ""
            for i in range(12):
                passwd = passwd + element[random.randint(0, 73)]

            # Chiffrement du nouveau mot de passe
            passwd_hash = hashlib.sha256(str(passwd).encode('utf-8')).hexdigest()

            # Envoi du nouveau mot de passe à la base de données
            sql_obj.modify_user_info_mdp(request.form['mail'], passwd_hash)

            # Envoi de l'email
            msg = MIMEMultipart()
            msg['From'] = config.email
            msg['To'] = request.form['mail']
            msg['Subject'] = 'BlaBla-Tutorat -- Nouveau mot de passe'
            message = 'Bonjour,\n\nNous avons généré pour vous un nouveau mot de passe : ' \
                      + passwd + '\nVeuillez le changer dès que vous vous connecterez à BlaBla-Tutorat.\n' \
                                 'L\'équipe de BlaBla-Tutorat vous souhaite une bonne journée.\n\n\n\n\nCet e-mail a été généré' \
                                 ' automatiquement, merci de ne pas y répondre.' \
                                 ' Pour toute question, veuillez vous adresser aux documentalistes.'
            msg.attach(MIMEText(message))
            mailserver = smtplib.SMTP(config.smtp, config.smtp_port)
            mailserver.starttls()
            mailserver.login(config.email, config.email_password)
            mailserver.sendmail(msg['From'], msg['To'], msg.as_string())
            mailserver.quit()
            return redirect(url_for('connexion', info_msg="Un nouveau mot de passe vous a été envoyé."))
        else:
            return redirect(url_for("mdp_oublie", info_msg="Cette adresse e-mail ne correspond à aucun compte"))
    else:
        return redirect(url_for("recherche"))


# Page de Profil info utilisateur
@app.route('/profile/view')
def profil():
    """Page de de profil avec les informations de l'utilisateur"""
    sql_obj = sql.MysqlObject()
    if request.args.get('delete'):
        delete_account = request.args.get('delete')
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
    """Page de profil avec la liste des offres et des demandes créées par l'utilisateur"""
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]
        demandes = sql_obj.get_user_demandes(mail)
        demandes_T = sql_obj.get_user_demandes_tuteur(mail)
        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')
        return render_template("profil/profil_t_p.html", offres_creees=sql_obj.get_user_offres(mail),
                               offres_suivies=sql_obj.get_user_offres_suivies(mail), days=days, **locals())
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page de suppression Profil
@app.route('/profile/delete')
def profil_3():
    """Supprime le compte utilisateur de la BDD"""
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        sql_obj.delete_account(mail)
        liste = sql_obj.get_user_offres_suivies(mail)
        for x in liste:
            sql_obj.delete_participant(x[0], mail)
        return redirect(url_for('connexion', info_msg="Votre compte a bien été supprimé."))
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page de profil d'un utilisateur
@app.route('/profile/view/<mail>')
def profil_4(mail):
    """Popup avec les informations de l'utilisateur qui correspond au mail cliqué"""
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
    """Page de mise à jour de profil, récolte les information données par l'utilisateur et les envoie à la BDD"""
    sql_obj = sql.MysqlObject()
    if check_connexion():
        if request.args.get('info_msg'):
            info_msg = request.args.get('info_msg')
        mail = session['mail']
        admin_user = check_admin()
        classes = sql_obj.classes_liste()
        if len(request.form) == 0:
            # Pas de formulaire envoyé, on charge la page normalement
            return render_template("profil/profil_update.html", infos=sql_obj.get_user_info(mail)[0], **locals())
        else:
            if request.form.get('classe') in classes:
                # Chiffrement du mdp
                if request.form.get('mdp') != '' and request.form.get('mdp2') != '':
                    chaine_mot_de_passe = request.form.get('mdp')
                    mdp_confirm = request.form.get('mdp2')
                    if chaine_mot_de_passe == mdp_confirm:
                        mot_de_passe_chiffre = hashlib.sha256(str(chaine_mot_de_passe).encode('utf-8')).hexdigest()
                        # Envoi des infos à la base de données
                        sql_obj.modify_user_info_mdp(mail, mot_de_passe_chiffre)
                mail2 = request.form.get('mail')
                # Envoi des infos à la base de données
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
    """Page d'administration qui affiche les offres en cours"""
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


# Page d'Administration demandes en courts
@app.route('/admin/tutorials/progress/demandes', methods=['GET', 'POST'])
def admin_oc2():
    """Page d'administration qui affiche les demandes en cours"""
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
                    return render_template("admin/admin_t_p_d.html",
                                           demandes=sql_obj.demandes_liste_tri_admin(user_search[0][2]),
                                           days=days, **locals())
                else:
                    # Pas d'utilisateur trouvé donc liste vide
                    return render_template("admin/admin_t_p_d.html", demandes=[], days=days,
                                           **locals())
            else:
                return render_template("admin/admin_t_p_d.html", demandes=sql_obj.demandes_liste_validees(),
                                       days=days, **locals())
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez vous avant de continuer.'))


# Page d'Administration offres à valider
@app.route('/admin/tutorials/validate')
def admin_ov():
    """Page d'administration qui affiche les offres et demandes à valider"""
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
            return render_template("admin/admin_t_v.html", offres_V=sql_obj.offres_liste_valider(),
                                   demandes_V=sql_obj.demandes_liste_valider(), days=days,
                                   **locals())
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez vous avant de continuer.'))


# Page d'Administration profile utilisateur
@app.route('/admin/users', methods=['GET', 'POST'])
def admin_u():
    """Page d'administration qui affiche la liste des utilisateurs du site"""
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
                                       tutorats_actifs=sql_obj.offres_liste_validees(),
                                       demandes=sql_obj.demandes_liste_validees(), days=days, **locals())
            else:
                return render_template("admin/admin_u.html", user_list=sql_obj.liste_user(),
                                       tutorats_actifs=sql_obj.offres_liste_validees(),
                                       demandes=sql_obj.demandes_liste_validees(), days=days, **locals())
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez vous avant de continuer.'))


# Page de recherche d'offres
@app.route('/search', methods=['GET', 'POST'])
def recherche():
    """Page de recherche"""
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

        if request.form.get("categorie") == "demande":
            # PARTIE DEMANDE

            if request.form.get("option"):
                # Formulaire de tri première étape
                option = request.form.get("option")

                if option == "suggestion":

                    suggest_d1 = sql_obj.get_tuteur_info(mail)[0]
                    suggest_d2 = sql_obj.get_tuteur_info(mail)[1]
                    return render_template("suggestion/suggest_d.html", days=days, **locals())

                else:
                    # Défaut car pas d'autre paramètres de tri
                    return render_template("recherche_demande.html", demandes=sql_obj.demandes_liste(page), days=days,
                                           **locals())
            else:
                # Aucune option de tri sélectionnée
                return render_template("recherche_demande.html", demandes=sql_obj.demandes_liste(page), days=days,
                                       **locals())

        else:
            # PARTIE OFFRE

            if request.form.get("option") and not request.form.get("option2"):
                # Formulaire de tri première étape
                option = request.form.get("option")

                # Cas spécial suggestions
                if option == "suggestion":

                    suggest_o1 = sql_obj.get_tutore_info(mail)[0]
                    suggest_o2 = sql_obj.get_tutore_info(mail)[1]
                    return render_template("suggestion/suggest_o.html", days=days, **locals())
                else:
                    return render_template("recherche_offre.html", offres=sql_obj.offres_liste_tri(option, page, mail),
                                           days=days,
                                           **locals())

            elif request.form.get("option") and request.form.get("option2"):
                # Formulaire de tri deuxième étape
                option = request.form.get("option")
                option2 = request.form.get("option2")
                return render_template("recherche_offre.html",
                                       offres=sql_obj.offres_liste_tri_2(option, option2, page, mail),
                                       days=days, **locals())
            else:
                # Aucune option de tri sélectionnée
                return render_template("recherche_offre.html", offres=sql_obj.offres_liste(page, mail), days=days,
                                       **locals())

    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Affichage du formulaire de création d'une offre
@app.route('/create', methods=['GET'])
def creation():
    """Page de création"""
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
    """Envoie les données rentrées par l'utilisateur à la BDD"""
    # On ne traite pas la demande dans le doute ou l'élève n'a pas renseigné de créneau horaire
    process = False
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']
        admin_user = check_admin()
        user = sql_obj.get_user_info(mail)[0][0]

        if len(request.form) == 1:
            # Changement offre/demande
            if request.form['categorie'] == "demande":
                # On definit la catégorie sur demande
                demande = True
                classe = sql_obj.get_user_info(mail)[0][3]
                return render_template("creation.html", filieres=sql_obj.filieres_liste(),
                                       matieres=sql_obj.matieres_liste(),
                                       days=days, **locals())
            else:
                # Sinon on charge la template de base
                return render_template("creation.html", filieres=sql_obj.filieres_liste(),
                                       matieres=sql_obj.matieres_liste(),
                                       days=days, **locals())
        else:
            # Suite du formulaire de création
            horaires = request.form["horaires_data"]
            if len([c for c in horaires if c == '1']) > 0:
                process = True

            if process:
                # Création
                filieres = sql_obj.filieres_liste()
                matieres = sql_obj.matieres_liste()
                if request.form.get("filiere"):
                    # OFFRE
                    if request.form.get("filiere") in filieres and request.form.get("matiere") in matieres:
                        sql_obj.create_offre(mail, request.form.get('filiere'),
                                             request.form.get('matiere'),
                                             horaires)
                        return redirect(url_for("recherche",
                                                info_msg="Votre offre a bien été créée. Elle est actuellement"
                                                         " en attente de validation."))
                    else:
                        return render_template("error.html",
                                               message="Erreur - Veuillez vérifier les champs du formulaire",
                                               **locals())
                else:
                    # DEMANDE
                    if request.form.get("matiere") in matieres:
                        sql_obj.create_demande(mail, request.form.get('classe'),
                                               request.form.get('matiere'),
                                               horaires)
                        return redirect(url_for("recherche",
                                                info_msg="Votre demande a bien été créée. Elle est actuellement"
                                                         " en attente de validation."))
                    else:
                        return render_template("error.html",
                                               message="Erreur - Veuillez vérifier les champs du formulaire",
                                               **locals())
            else:
                # Erreur
                return render_template("error.html", message="Erreur - Veuillez renseigner au moins un horaire",
                                       **locals())
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Page d'enregistrement (s'enregistrer en tant que participant)
@app.route('/apply', methods=['POST'])
def enregistrement():
    """Enregistre l'utilisateur comme participant à ce tutorat"""
    sql_obj = sql.MysqlObject()
    if check_connexion():
        mail = session['mail']

        if request.form.get("categorie") == "demande":
            result_code = sql_obj.add_tuteur(request.form.get("id"), mail)
        else:
            result_code = sql_obj.add_participant(request.form.get("id"), mail)

        if result_code == 0:
            # Pas d'erreur
            if request.form.get("categorie") == "demande":
                return redirect(url_for("select_2", tutorat_id=request.form.get("id")))
            else:
                return redirect(url_for("select", tutorat_id=request.form.get("id")))
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


# Selection horaires (offre)
@app.route('/select', methods=['GET', 'POST'])
def select():
    """Selection des horaires pour les offres"""
    if check_connexion():
        mail = session['mail']
        sql_obj = sql.MysqlObject()
        admin_user = check_admin()
        if request.args.get('tutorat_id'):
            id_offre = request.args.get('tutorat_id')

            if mail == sql_obj.get_offre(id_offre)[5]:
                return render_template("select_horaires.html", o=sql_obj.get_offre(id_offre), days=days,
                                       **locals())
            elif mail == sql_obj.get_offre(id_offre)[6]:
                return redirect(
                    url_for("recherche", info_msg="Vous avez bien été ajouté en tant que participant à ce tutorat."))
            else:
                abort(403)

        elif len(request.form) != 0:
            horaires = request.form["horaires_data"]
            sql_obj.modifier_offre(request.form.get("id"), horaires)
            return redirect(
                url_for("recherche", info_msg="Vous avez bien été ajouté en tant que participant à ce tutorat."))

        else:
            abort(404)

    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Selection horaires (demande)
@app.route('/select_2', methods=['GET', 'POST'])
def select_2():
    """Selection des horaires pour les demandes"""
    if check_connexion():
        mail = session['mail']
        sql_obj = sql.MysqlObject()
        admin_user = check_admin()
        if request.args.get('tutorat_id'):
            id_demande = request.args.get('tutorat_id')

            if mail == sql_obj.get_demande(id_demande)[5]:
                return render_template("select_horaires_d.html", o=sql_obj.get_demande(id_demande), days=days,
                                       **locals())
            else:
                abort(403)

        elif len(request.form) != 0:
            horaires = request.form["horaires_data"]
            sql_obj.modifier_demande(request.form.get("id"), horaires)
            return redirect(url_for("recherche", info_msg="Vous avez bien été ajouté en tant que tuteur."))

        else:
            abort(404)

    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Modification d'une demande (affichage)
@app.route('/edit_d')
def modifier_demande():
    """Modification d'une demande"""
    if check_connexion():
        mail = session['mail']
        if request.args.get('id'):
            sql_obj = sql.MysqlObject()
            admin_user = check_admin()
            demande_id = request.args.get('id')
            # Vérification que l'auteur est celui qui demande la suppression
            if mail == sql_obj.get_demande(demande_id)[1]:
                return render_template("edit/edit_d.html", demande=sql_obj.get_demande(demande_id),
                                       filieres=sql_obj.filieres_liste(), matieres=sql_obj.matieres_liste(),
                                       days=days, **locals())
            else:
                abort(403)
        else:
            abort(403)

    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Modification d'une offre (affichage)
@app.route('/edit_o')
def modifier_offre():
    """Modification d'une offre"""
    if check_connexion():
        mail = session['mail']
        if request.args.get('id'):
            sql_obj = sql.MysqlObject()
            admin_user = check_admin()
            offre_id = request.args.get('id')
            # Vérification que l'auteur est celui qui demande la suppression
            if mail == sql_obj.get_offre(offre_id)[1]:
                return render_template("edit/edit_o.html", offre=sql_obj.get_offre(offre_id),
                                       filieres=sql_obj.filieres_liste(), matieres=sql_obj.matieres_liste(),
                                       days=days, **locals())
            else:
                abort(403)
        else:
            abort(403)

    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Modification d'une offre/demande (formulaire)
@app.route('/edit_apply', methods=['POST'])
def modification_offre_demande():
    """Modification d'une offre"""
    if check_connexion():
        sql_obj = sql.MysqlObject()
        mail = session['mail']
        id = request.form.get('id')
        horaires = request.form.get('horaires_data')

        if request.form.get('categorie') == "demande":
            # Demande
            demande = sql_obj.get_demande(id)
            # Vérification que l'auteur est celui qui demande la modification
            if mail == demande[1]:
                sql_obj.modifier_demande(id, horaires)
            else:
                abort(403)
        else:
            # Offre
            offre = sql_obj.get_offre(id)
            # Vérification que l'auteur est celui qui demande la modification
            if mail == offre[1]:
                sql_obj.modifier_offre(id, horaires)
            else:
                abort(403)

        return redirect(url_for("profil_2"))
    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Suppression de la participation d'un utilisateur à une offre
@app.route('/quit')
def quit_tutorat():
    """Sert à quitter un tutorat"""
    sql_obj = sql.MysqlObject()
    if check_connexion():
        if request.args.get('id'):
            offre_id = request.args.get('id')
            mail = session['mail']
            if sql_obj.delete_participant(offre_id, mail):
                return redirect(url_for("profil_2", info_msg="Votre retrait de ce Tutorat a bien été enregistré."))
            else:
                return redirect(url_for("profil_2", info_msg="Vous ne participez pas à ce Tutorat"))
        else:
            abort(403)
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Suppression de la participation d'un utilisateur à une offre
@app.route('/quit_2')
def quit_2():
    """Sert à quitter une demande"""
    sql_obj = sql.MysqlObject()
    if check_connexion():
        if request.args.get('id'):
            demande_id = request.args.get('id')
            mail = session['mail']
            if sql_obj.quit_demande(demande_id, mail):
                return redirect(url_for("profil_2", info_msg="Votre retrait de ce Tutorat a bien été enregistré."))
            else:
                return redirect(url_for("profil_2", info_msg="Vous ne participez pas à ce Tutorat"))
        else:
            abort(403)
    else:
        # Redirection si l'utilisateur n'est pas connecté
        return redirect(url_for('connexion', info_msg="Veuillez vous connecter pour continuer."))


# Suppression d'une offre
@app.route('/delete')
def delete():
    """Supprime une offre"""
    if check_connexion():
        mail = session['mail']
        if request.args.get('id'):
            sql_obj = sql.MysqlObject()
            offre_id = request.args.get('id')
            offre = sql_obj.get_offre(offre_id)
            # Vérification que l'auteur est celui qui demande la suppression
            if mail == offre[1]:
                sql_obj.delete_offer(offre_id)
                return redirect(url_for("profil", info_msg="Votre offre a bien été supprimée."))
            else:
                abort(403)
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Suppression d'une demande
@app.route('/delete3')
def delete3():
    """Supprime une demande"""
    if check_connexion():
        mail = session['mail']
        if request.args.get('id'):
            sql_obj = sql.MysqlObject()
            demande_id = request.args.get('id')
            demande = sql_obj.get_demande(demande_id)
            # Vérification que l'auteur est celui qui demande la suppression
            if mail == demande[1]:
                sql_obj.delete_demande(demande_id)
                return redirect(url_for("profil", info_msg="Votre demande a bien été supprimée."))
            else:
                abort(403)
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Suppression d'une offre (admin)
@app.route('/delete2')
def delete2():
    """Supprime une offre (version admin)"""
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


# Suppression d'une demande (admin)
@app.route('/delete4')
def delete4():
    """Supprime une demande (version admin)"""
    if check_connexion():
        admin_user = check_admin()
        if admin_user:
            if request.args.get('id'):
                demande_id = request.args.get('id')
                sql_obj = sql.MysqlObject()
                sql_obj.delete_demande(demande_id)
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
    """Sert à valider une offre"""
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


# Validation d'une demande (admin)
@app.route('/validate2')
def validate2():
    """Sert à valider une demande"""
    if check_connexion():
        admin_user = check_admin()
        if admin_user:
            if request.args.get('id'):
                disponible = 1
                demande_id = request.args.get('id')
                sql_obj = sql.MysqlObject()
                sql_obj.validate_demande(demande_id, disponible)
                return redirect(url_for("admin_ov", info_msg="La demande a bien été validée."))
            else:
                abort(403)
        else:
            abort(403)
    else:
        return redirect(url_for("connexion", info_msg='Connectez-vous avant de continuer.'))


# Ban (admin)
@app.route('/ban')
def ban():
    """Bannis un utilisateur"""
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
    """Promouvois un utilisateur admin"""
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


# Déconnexion
@app.route('/disconnect')
def deconnexion():
    """Sert à se déconnecter du site"""
    if check_connexion():
        session.pop('mail', None)
        return redirect(url_for("connexion", info_msg='Vous avez bien été déconnecté.'))
    else:
        return redirect(url_for("connexion"))


# Remise à 0
@app.route('/reset')
def reset():
    """Remet à 0 le site"""
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
    """Affiche la page erreur 404"""
    return render_template("error.html", message="Erreur 404 - Ressource non trouvée", **locals())


# Gestion de l'erreur 403
@app.errorhandler(403)
def forbidden(error):
    """Affiche la page erreur 403"""
    return render_template("error.html", message="Erreur 403 - Accès Interdit", **locals())


# Gestion de l'erreur 405
@app.errorhandler(405)
def method_not_allowed(error):
    """Affiche la page erreur 405"""
    return render_template("error.html", message="Erreur 405 - Méthode de requête non autorisée", **locals())


# Vérification connexion
def check_connexion():
    """Vérifie si l'utilisateur est connecté"""
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
    """Vérifie si l'utilisateur est admin"""
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
app.secret_key = config.secret_key


# Lancement du serveur lors de l'exécution du fichier
if __name__ == '__main__':
    app.run()
