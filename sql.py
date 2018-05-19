# coding: utf-8
import datetime
import sys

import mysql.connector

import config
import utils

offres_par_page = 4


class MysqlObject:
    # Méthode executée à la création de l'objet
    def __init__(self):
        """Méthode executée à la création de l'objet"""
        try:
            self.conn = mysql.connector.connect(host=config.host, user=config.user, password=config.password,
                                                database=config.database)
            self.cursor = self.conn.cursor()
        except mysql.connector.errors.InterfaceError as e:
            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

    # Méthode exécutée à la suppression de l'objet
    def __del__(self):
        """Méthode exécutée à la suppression de l'objet"""
        self.cursor.close()
        self.conn.close()

    """
        REQUETES GENERALES SUR LA BDD
    """

    # Liste des classes
    def classes_liste(self):
        """Renvoie la liste des classes"""
        classes = []
        self.cursor.execute("""SELECT * FROM classes""")
        rows = self.cursor.fetchall()
        # On ne retourne que le nom
        for row in rows:
            if row[0] != "ADMIN":
                classes.append(row[0])
        return classes

    # Liste des matières
    def matieres_liste(self):
        """Renvoie la liste des matières"""
        matieres = []
        self.cursor.execute("""SELECT * FROM matieres""")
        rows = self.cursor.fetchall()
        # On ne retourne que le nom
        for row in rows:
            matieres.append(row[0])
        return matieres

    # Liste des filières
    def filieres_liste(self):
        """Renvoie la liste des filières"""
        filieres = []
        self.cursor.execute("""SELECT * FROM filieres""")
        rows = self.cursor.fetchall()
        # On ne retourne que le nom
        for row in rows:
            filieres.append(row[0])
        return filieres

    """
        REQUETES CONCERNANT LES UTILISATEURS SUR LA BDD
    """

    # Listes des utilisateurs
    def delete_account(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Suprime le compte utilisateur de la BDD et les offres et demandes créées par l'utilisateur"""
        self.cursor.execute("""DELETE FROM users WHERE mail = %s""", (mail,))
        self.cursor.execute("""DELETE FROM offres WHERE auteur = %s""", (mail,))
        self.cursor.execute("""DELETE FROM demandes WHERE auteur = %s""", (mail,))
        self.conn.commit()

    # Listes des utilisateurs
    def liste_user(self):
        """Renvoie la liste des utilisateurs du site"""
        self.cursor.execute("""SELECT * FROM users""")
        return self.cursor.fetchall()

    # Vérifier si le mail existe
    def mail_in_bdd(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Vérifie si le mail existe"""
        self.cursor.execute("""SELECT mail FROM users WHERE mail =%s""", (mail,))
        if len(self.cursor.fetchall()) != 0:
            return True
        else:
            return False

    # Récupération des infos utilisateurs par mail
    def get_user_info(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Renvoie les données de l'utilisateur"""
        self.cursor.execute("""SELECT * FROM users WHERE mail=%s""", (mail,))
        return self.cursor.fetchall()

    # Récupération des infos utilisateurs par pseudo ( ADMIN UNIQUEMENT )
    def get_user_info_pseudo(self, user_search):
        """Argument: Pseudo de l'utilisateur
        Fonction: renvoie les données de l'utilisateur"""
        self.cursor.execute("""SELECT * FROM users WHERE nom = %s""", (user_search,))
        return self.cursor.fetchall()

    # Mail vers pseudo ( le mail existe )
    def get_user_pseudo(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Renvoie le pseudo de l'utilisateur"""
        self.cursor.execute("""SELECT nom FROM users WHERE mail=%s""", (mail,))
        return self.cursor.fetchall()[0][0]

    # Pseudo vers mail ( l'utilisateur existe )
    def get_user_mail(self, user):
        """Argument: Pseudo de l'utilisateur
        Fonction: Renvoie le mail de l'utilisteur"""
        self.cursor.execute("""SELECT mail FROM users WHERE nom=%s""", (user,))
        return self.cursor.fetchall()[0][0]

    # Récupération du mot de passe crypté des utilisateurs
    def get_crypt_mdp(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Renvoie le mot de passe crypté de l'utilisateur"""
        self.cursor.execute("""SELECT mdp FROM users WHERE mail=%s""", (mail,))
        return self.cursor.fetchall()

    # Check ban
    def check_ban(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Vérifie si l'utilisateur est bannis"""
        self.cursor.execute("""SELECT ban FROM users WHERE mail=%s""", (mail,))
        if self.cursor.fetchall()[0][0] == 1:
            # L'utilisateur est ban
            return True
        else:
            # L'utiliasteur n'est pas ban
            return False

    """
        REQUETES CONCERNANT LES OFFRES SUR LA BDD
    """

    # Recherche des offres auxquelles participe l'utilisateur
    def get_user_offres_suivies(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Renvoie les offre auxquelles participe l'utilisateur"""
        self.cursor.execute("""SELECT * FROM offres WHERE participant=%s OR participant2=%s""", (mail, mail))
        return self.cursor.fetchall()

    # Récupération des offres créées par un utilisateur
    def get_user_offres(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Renvoie les offres créées par l'utilisateur"""
        self.cursor.execute("""SELECT * FROM offres WHERE auteur=%s""", (mail,))
        return self.cursor.fetchall()

    # Listes des offres à valider
    def offres_liste_valider(self):
        """Renvoie la liste des offres à valider"""
        self.cursor.execute("""SELECT * FROM offres WHERE disponible=0""")
        return self.cursor.fetchall()

    # Listes des offres validées
    def offres_liste_validees(self):
        """Renvoie la liste des offres qui ont été validées"""
        self.cursor.execute("""SELECT * FROM offres WHERE disponible=1""")
        return self.cursor.fetchall()

    # Récupération d'une offre
    def get_offre(self, offer_id):
        """Argument: Id de l'offre
        Fonction: Renvoie l'offre"""
        self.cursor.execute("""SELECT * FROM offres WHERE id = %s""", (offer_id,))
        return self.cursor.fetchall()

    # Listes des offres
    def offres_liste(self, page, mail):
        """Argument: Mail de l'utilisateur, numéro de la page
        Fonction: Renvoie la liste des offres valide pour l'utilisateur"""
        classe = self.get_user_info(mail)[0][3]
        offres = []
        self.cursor.execute(
            """SELECT * FROM offres WHERE disponible=1 AND (participant IS NULL OR participant2 IS NULL) LIMIT """ +
            str(offres_par_page) + """ OFFSET """ + str(page * offres_par_page))
        rows = self.cursor.fetchall()
        # Tri des offres pour ne garder que celles où la classe du 1er participant est identique à celle de user
        for row in rows:
            if row[5] is None:
                offres.append(row)
            else:
                if classe == self.get_user_info(row[5])[0][3]:
                    offres.append(row)
        return offres

    # Liste des offres selon 1 facteur de tri
    def offres_liste_tri(self, option, page, mail):
        """Argument: Mail de l'utilisateur, numéro de page, option de tri choisi
        Fonction: Renvoie la liste des offres valide pour l'utilisateur et trié"""
        classe = self.get_user_info(mail)[0][3]
        offres = []
        self.cursor.execute(
            """SELECT * FROM offres WHERE disponible=1 AND (participant IS NULL OR participant2 IS NULL) ORDER BY """
            + option + """ LIMIT """ + str(offres_par_page) + """ OFFSET """ + str(page * offres_par_page))
        rows = self.cursor.fetchall()
        # Tri des offres pour ne garder que celles où la classe du 1er participant est identique à celle de user
        for row in rows:
            if row[5] is None:
                offres.append(row)
            else:
                if classe == self.get_user_info(row[5])[0][3]:
                    offres.append(row)
        return offres

    # Obtenir niveau élève
    def classe_to_niveau(self, classe):
        self.cursor.execute("""SELECT niveau FROM filieres WHERE classe=%s""", (classe,))
        return self.cursor.fetchall()[0][0]

    # Informations des demandes d'un certain utilisateur
    def demandes_info(self, mail):
        self.cursor.execute("""SELECT * FROM demandes WHERE auteur=%s""", (mail,))
        return self.cursor.fetchall()

    # Informations de toutes les offres créées
    def offres_info(self, mail):
        classe_o = self.get_user_info(mail)[0][3]
        niveau_o = self.classe_to_niveau(classe_o)
        self.cursor.execute("""SELECT * FROM offres""")
        return self.cursor.fetchall(), niveau_o

    # Liste des offres selon 1 facteur de tri + 1 niveau/matiere
    def offres_liste_tri_2(self, option, option2, page, mail):
        """Argument: Mail de l'utilisateur, numéro de page, option de tri 1, option de tri 2
        Fonction: Renvoie la liste des offres valide pour l'utilisateur et trié"""
        classe = self.get_user_info(mail)[0][3]
        offres = []
        self.cursor.execute(
            """SELECT * FROM offres WHERE disponible=1 AND (participant IS NULL OR participant2 IS NULL)
             AND """ + option + """ = '""" + option2 + """' LIMIT """ + str(offres_par_page) + """ OFFSET """ + str(
                page * offres_par_page))
        rows = self.cursor.fetchall()
        # Tri des offres pour ne garder que celles où la classe du 1er participant est identique à celle de user
        for row in rows:
            if row[5] is None:
                offres.append(row)
            else:
                if classe == self.get_user_info(row[5])[0][3]:
                    offres.append(row)
        return offres

    # Listes des offres tri admin
    def offres_liste_tri_admin(self, user_search):
        """Argument: Mail de l'utilisateur
        Fonction: Renvoie la liste des offres quand on recherche un utilisateur"""
        self.cursor.execute(
            """SELECT * FROM offres WHERE auteur = %s OR participant = %s OR participant2 = %s AND disponible=1""",
            (user_search, user_search, user_search))
        return self.cursor.fetchall()

    # Création d"une offre
    def create_offre(self, author, classe, matiere, horaires):
        """Argument: Mail de l'utilisateur, Filière, matière, horraires
        Fonction: Envoie les infos à la BDD et créer l'offre"""
        date_time = datetime.datetime.now()
        date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            """INSERT INTO offres (auteur, filiere, matiere, date_time, horaires) VALUES (%s, %s, %s, %s, %s)""",
            (author, classe, matiere, date_time, horaires))
        self.conn.commit()

    # Suppression d'une offre
    def delete_offer(self, offre_id):
        """Argument: Id de l'offre
        Fonction: Surpime l'offre"""
        self.cursor.execute("""DELETE FROM offres WHERE id = %s""", (offre_id,))
        self.conn.commit()

    # Ajout de participant à une offre
    def add_participant(self, offre_id, participant):
        """Argument: Id de l'offre, mail du participant
        Fonction: Ajoute un participant à une offre"""
        self.cursor.execute("""SELECT * FROM offres WHERE id=%s""", (offre_id,))
        offre = self.cursor.fetchall()[0]
        if offre[1] != participant:
            if utils.check_availability(offre) == 2:
                # Update de la première colonne
                self.cursor.execute("""UPDATE offres SET participant = %s WHERE id = %s """, (participant, offre_id))
                self.conn.commit()
                return 0
            elif utils.check_availability(offre) == 1:
                # Update de la deuxième colonne + check si l'utilisateur n'est pas déjà participant à cette offre
                if offre[5] != participant:
                    # Check si l'utilisateur est dans la même classe que le premier
                    if self.get_user_info(participant)[0][3] == self.get_user_info(offre[5])[0][3]:
                        self.cursor.execute("""UPDATE offres SET participant2 = %s WHERE id = %s """,
                                            (participant, offre_id))
                        self.conn.commit()
                        return 0
                    else:
                        # Erreur l'utilisateur n'est pas dans la même classe que le premier
                        return 4
                else:
                    # Erreur l'utilisateur participe déjà à ce tutorat
                    return 1
            else:
                # Erreur l'offre est pleine
                return 2
        else:
            # auteur == tuteur
            return 3

    # Suppression d'un participant à une offre
    def delete_participant(self, offre_id, mail):
        """Argument: Id de l'offre, mail du participant
        Fonction: Surpime le paticipant de l'offre"""
        self.cursor.execute("""SELECT * FROM offres WHERE id=%s""", (offre_id,))
        offres_a_modif = self.cursor.fetchall()
        if len(offres_a_modif) == 1:
            offre_a_modif = offres_a_modif[0]
            places_dispo = utils.check_availability(offre_a_modif)
            if places_dispo == 0:
                if offre_a_modif[5] == mail:
                    self.cursor.execute(
                        """UPDATE offres SET participant = participant2, participant2 = NULL WHERE id = %s """,
                        (offre_id,))
                    self.conn.commit()
                    return True
                elif offre_a_modif[6] == mail:
                    self.cursor.execute("""UPDATE offres SET participant2 = NULL WHERE id = %s """, (offre_id,))
                    self.conn.commit()
                    return True
                else:
                    # L'utilisateur ne participe pas au Tutorat
                    return False
            elif places_dispo == 1:
                if offre_a_modif[5] == mail:
                    self.cursor.execute("""UPDATE offres SET participant = NULL WHERE id = %s """, (offre_id,))
                    self.conn.commit()
                    return True
                else:
                    # L'utilisateur ne participe pas au Tutorat
                    return False
            else:
                # L'utilisateur ne participe pas au Tutorat
                return False
        else:
            return False

    # Validation d'une offre
    def validate_offer(self, offre_id, disponible):
        self.cursor.execute("""UPDATE offres SET disponible = %s WHERE id = %s""", (disponible, offre_id))
        self.conn.commit()

    # Modification d'une offre
    def modifier_offre(self, offre_id, horaires):
        self.cursor.execute("""UPDATE offres SET horaires = %s WHERE id = %s""", (horaires, offre_id))
        self.conn.commit()

    """
        REQUETES DIVERSES SUR LA BDD
    """

    # Ban
    def ban(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Bannis l'utilisateur"""
        self.cursor.execute("""UPDATE users SET ban = NOT ban WHERE mail = %s""", (mail,))
        self.cursor.execute("""DELETE FROM offres WHERE auteur = %s""", (mail,))
        self.conn.commit()

    # Promouvoir
    def promote(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Promouvois admin l'utilisateur"""
        self.cursor.execute("""UPDATE users SET classe = 'ADMIN' WHERE mail = %s""", (mail,))
        self.conn.commit()

    # Modification du profil Classe
    def modify_user_info(self, mail, classe):
        """Argument: Mail de l'utilisateur, classe choisi
        Fonction: Modifie la classe de l'utilisateur"""
        self.cursor.execute("""UPDATE users SET classe = %s WHERE mail = %s """, (classe, mail))
        self.conn.commit()

    # Modification du profil mail
    def modify_user_info_mail(self, mail, mail2):
        """Argument: Mail de l'utilisateur, nouveau mail
        Fonction: Modifie le mai lde l'utilisateur"""
        self.cursor.execute("""UPDATE users SET mail = %s WHERE mail = %s """, (mail2, mail))
        self.conn.commit()

    # Modification du profil mdp
    def modify_user_info_mdp(self, mail, mdp):
        """Argument: Mail de l'utilisateur, mot de passe
        Fonction: Modifie le mdp de l'utilisateur"""
        self.cursor.execute("""UPDATE users SET mdp = %s WHERE mail = %s """, (mdp, mail))
        self.conn.commit()

    # Création d'un compte
    def create_compte(self, nom, mdp, mail, classe):
        """Argument: Mail de l'utilisateur, nom, mot de passe, classe
        Fonction: Envoie les données à la BDD et créer un compte utilisateur"""
        self.cursor.execute(
            """INSERT INTO users (nom, mdp, mail, classe) VALUES (%s, %s, %s, %s)""", (nom, mdp, mail, classe))
        self.conn.commit()

    # Reset
    def reset(self):
        """Remet le site a 0"""
        self.cursor.execute("""DELETE FROM `users` WHERE classe != 'ADMIN'""")
        self.cursor.execute("""DELETE FROM `offres`""")
        self.conn.commit()

    # Retourne les informations pour les statistiques :
    def stat_nombre(self):
        """Retourne les informations pour les statistiques"""
        self.cursor.execute("""SELECT * FROM users""")
        # nombre d'utilisateurs
        n = 0
        for _ in self.cursor.fetchall():
            n += 1
        return n

    # nombre d'offres :
    def stat_offres(self):
        """Retourne le nombre d'offres"""
        self.cursor.execute("""SELECT * FROM offres""")
        o = 0
        for _ in self.cursor.fetchall():
            o += 1
        return o

    """
        REQUETES CONCERNANT LES DEMANDES SUR LA BDD
    """

    # nombre de tutoré
    def stat_demandes(self):
        """Retourne le nombre de tutoré"""
        self.cursor.execute(""" SELECT * FROM demandes""")
        d = 0
        for _ in self.cursor.fetchall():
            d += 1
        return d

    # Suppression d'une demande
    def delete_demande(self, demande_id):
        """Argument: id de la demande
        Fonction: Suprime l'offre"""
        self.cursor.execute("""DELETE FROM demandes WHERE id = %s""", (demande_id,))
        self.conn.commit()

    # Création d'une demande
    def create_demande(self, author, classe, matiere, horaires):
        """Argument: Mail de l'auteur, Filière, Matière, Horaires
        Fonction: Envoie les infos à la BDD et créer la demande"""
        date_time = datetime.datetime.now()
        date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            """INSERT INTO demandes (auteur, classe, matiere, date_time, horaires) VALUES (%s, %s, %s, %s, %s)""",
            (author, classe, matiere, date_time, horaires))
        self.conn.commit()

    # Récupération d'une demande
    def get_demande(self, demande_id):
        """Argument: Id de la demande
        Fonction: Renvoie la demande"""
        self.cursor.execute("""SELECT * FROM demandes WHERE id = %s""", (demande_id,))
        return self.cursor.fetchall()

    # Liste demandes sans tri
    def demandes_liste(self, page):
        """Argument: numéro de la page
        Fonction: Renvoie la liste des demande"""
        self.cursor.execute(
            """SELECT * FROM demandes WHERE disponible=1 AND tuteur IS NULL LIMIT """ +
            str(offres_par_page) + """ OFFSET """ + str(page * offres_par_page))
        return self.cursor.fetchall()

    # Liste demandes utilisateur
    def get_user_demandes(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Renvoie la liste des demandes créées par l'utilisateur"""
        self.cursor.execute(
            """SELECT * FROM demandes WHERE auteur=%s""", (mail,))
        return self.cursor.fetchall()

    # Liste demandes utilisateur
    def get_user_demandes_tuteur(self, mail):
        """Argument: Mail de l'utilisateur
        Fonction: Renvoie la liste des demandes où l'utilisateur est le tuteur"""
        self.cursor.execute(
            """SELECT * FROM demandes WHERE tuteur=%s""", (mail,))
        return self.cursor.fetchall()

    # Listes des demandes à valider
    def demandes_liste_valider(self):
        """Renvoie la liste des demandes à valider"""
        self.cursor.execute("""SELECT * FROM demandes WHERE disponible=0""")
        return self.cursor.fetchall()

    # Quitter une demande
    def quit_demande(self, id, mail):
        """Quitte la demande"""
        self.cursor.execute("""UPDATE demandes SET tuteur = NULL WHERE id = %s AND tuteur = %s""", (id, mail,))
        self.conn.commit()

    # Listes des demandes validées
    def demandes_liste_validees(self):
        """Renvoie la liste des demandes qui ont été validé"""
        self.cursor.execute("""SELECT * FROM demandes WHERE disponible=1""")
        return self.cursor.fetchall()

    # Validation d'une demande
    def validate_demande(self, demande_id, disponible):
        """Argument: id de la demande, disponible
        Fonction: Valide une demande"""
        self.cursor.execute("""UPDATE demandes SET disponible = %s WHERE id = %s""", (disponible, demande_id))
        self.conn.commit()

    # Listes des offres tri admin
    def demandes_liste_tri_admin(self, user_search):
        """Argument: Mail de l'utilisateur
        Fonction: Renvoie la liste des demande e nfonction de l'utilisateur recherché"""
        self.cursor.execute(
            """SELECT * FROM demandes WHERE auteur = %s OR tuteur = %s AND disponible=1""",
            (user_search, user_search))
        return self.cursor.fetchall()

    # Ajout tuteur à une demande
    def add_tuteur(self, demande_id, mail):
        """Argument: id de la demande, mail de l'utilisateur
        Fonction: Ajoute un tuteur a la demande"""
        self.cursor.execute("""SELECT * FROM demandes WHERE id=%s""", (demande_id,))
        demande = self.cursor.fetchall()[0]
        if demande[1] != mail:
            if demande[5] is None:
                # Update de la première colonne
                self.cursor.execute("""UPDATE demandes SET tuteur = %s WHERE id = %s """, (mail, demande_id))
                self.conn.commit()
                return 0
            else:
                # Erreur l'offre est pleine
                return 2
        else:
            # auteur == tuteur
            return 3

    # Modification d'une demande
    def modifier_demande(self, demande_id, horaires):
        self.cursor.execute("""UPDATE demandes SET horaires = %s WHERE id = %s""", (horaires, demande_id))
        self.conn.commit()

    # Offres
    def get_all_offres(self):
        self.cursor.execute("""SELECT * FROM offres""")
        offres = self.cursor.fetchall()
        return offres

    def get_all_demandes(self):
        self.cursor.execute("""SELECT * FROM demandes""")
        demandes = self.cursor.fetchall()
        return demandes

    def get_offres(self, mail):
        self.cursor.execute("""SELECT * FROM offres WHERE auteur = %s""", (mail,))
        offres_mail = self.cursor.fetchall()
        return offres_mail

    # Niveau classe
    def get_class_level(self, classe):
        self.cursor.execute("""SELECT classement FROM classes WHERE NOM = %s""", (classe,))
        lvl = self.cursor.fetchall()[0]
        return lvl

    # Niveau filière
    def get_filiere_level(self, filiere):
        self.cursor.execute("""SELECT classement FROM filieres WHERE nom = %s""", (filiere,))
        lvl_o = self.cursor.fetchall()[0]
        return lvl_o

    # Suggestion

    # Offres
    def get_tutore_info(self, mail):
        demandes = self.get_user_demandes(mail)

        # liste des suggestions de niveau 1 :
        suggest_d1 = []
        # Liste des suggestions de niveau 2 :
        suggest_d2 = []

        for demande in demandes:

            # variables demandes :
            matiere = demande[3]
            classe = demande[2]
            lvl = self.get_class_level(classe)
            horaires = demande[7]

            offres = self.get_all_offres()

            for x in offres:

                # variables offres :

                classe_o = x[2]
                lvl_o = self.get_filiere_level(classe_o)
                matiere_o = x[3]
                horaires_o = x[8]

                if lvl_o >= lvl and matiere == matiere_o:
                    suggest_d1.append(x)
                    n = 0
                    for y in horaires:
                        for z in horaires_o:
                            if y == z:
                                n += 1

                    if n >= 1:
                        suggest_d2.append(x)
                        del suggest_d1[-1]
        return suggest_d1, suggest_d2

    # Demandes

    def get_tuteur_info(self, mail):
        offres = self.get_offres(mail)

        # liste des suggestions de niveau 1 :
        suggest_o1 = []
        # Liste des suggestions de niveau 2 :
        suggest_o2 = []

        for offre in offres:

            # variables offres :
            matiere = offre[3]
            filiere = offre[2]
            lvl = self.get_filiere_level(filiere)
            horaires = offre[7]

            demandes = self.get_all_demandes()

            for x in demandes:

                # variables offres :

                classe_d = x[2]
                lvl_d = self.get_class_level(classe_d)
                matiere_d = x[3]
                horaires_d = x[7]

                if lvl >= lvl_d and matiere == matiere_d:
                    suggest_o1.append(x)
                    n = 0
                    for y in horaires:
                        for z in horaires_d:
                            if y == z:
                                n += 1

                    if n >= 1:
                        suggest_o2.append(x)
                        del suggest_o1[-1]
        return suggest_o1, suggest_o2
