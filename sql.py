# coding: utf-8
import datetime
import sys

import mysql.connector

import config

horaires_reference = ["debut_j0", "fin_j0", "debut_j1", "fin_j1", "debut_j2", "fin_j2", "debut_j3", "fin_j3",
                      "debut_j4", "fin_j4", "debut_j5", "fin_j5"]
offre_par_page = 4


class MysqlObject:

    # Méthode executée à la création de l'objet
    def __init__(self):

        try:

            self.conn = mysql.connector.connect(host=config.host, user=config.user, password=config.password,
                                                database=config.database)
            self.cursor = self.conn.cursor()

        except mysql.connector.errors.InterfaceError as e:

            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

    # Méthode exécutée à la suppression de l'objet
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    """
        REQUETES GENERALES SUR LA BDD
    """

    # Liste des classes
    def classes_liste(self):
        classes = []
        self.cursor.execute("""SELECT * FROM classes ORDER BY NUMERO""")
        rows = self.cursor.fetchall()
        # On ne retourne que le nom
        for row in rows:
            classes.append(row[2])
        return classes

    # Liste des matières
    def matieres_liste(self):
        matieres = []
        self.cursor.execute("""SELECT * FROM matieres""")
        rows = self.cursor.fetchall()
        # On ne retourne que le nom
        for row in rows:
            matieres.append(row[2])
        return matieres

    # Liste des filières
    def filieres_liste(self):
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
    def liste_user(self):
        self.cursor.execute("""SELECT * FROM users""")
        return self.cursor.fetchall()

    # Vérifier si le mail existe
    def mail_in_bdd(self, mail):
        self.cursor.execute("""SELECT mail FROM users WHERE mail =%s""", (mail,))
        if len(self.cursor.fetchall()) != 0:
            return True
        else:
            return False

    # Récupération des infos utilisateurs par mail
    def get_user_info(self, mail):
        self.cursor.execute("""SELECT * FROM users WHERE mail=%s""", (mail,))
        return self.cursor.fetchall()

    # Récupération des infos utilisateurs par pseudo ( ADMIN UNIQUEMENT )
    def get_user_info_pseudo(self, user_search):
        self.cursor.execute("""SELECT * FROM users WHERE nom = %s""", (user_search,))
        return self.cursor.fetchall()

    # Mail vers pseudo ( le mail existe )
    def get_user_pseudo(self, mail):
        self.cursor.execute("""SELECT nom FROM users WHERE mail=%s""", (mail,))
        return self.cursor.fetchall()[0][0]

    # Pseudo vers mail ( l'utilisateur existe )
    def get_user_mail(self, user):
        self.cursor.execute("""SELECT mail FROM users WHERE nom=%s""", (user,))
        return self.cursor.fetchall()[0][0]

    # Récupération et cryptage du mot de passe des utilisateurs
    def get_crypt_mdp(self, mail):
        self.cursor.execute("""SELECT mdp FROM users WHERE mail=%s""", (mail,))
        return self.cursor.fetchall()

    """
        REQUETES CONCERNANT LES OFFRES SUR LA BDD
    """

    # Recherche des offres auxquelles participe l'utilisateur
    def get_user_tutorats(self, mail):
        self.cursor.execute("""SELECT * FROM offres WHERE participant=%s OR participant2=%s""", (mail, mail))
        return self.cursor.fetchall()

    # Récupération des offres propres à un utilisateur
    def get_user_offres(self, mail):
        self.cursor.execute("""SELECT * FROM offres WHERE auteur=%s""", (mail,))
        return self.cursor.fetchall()

    # Listes des offres à valider
    def offres_liste_valider(self):
        self.cursor.execute("""SELECT * FROM offres WHERE disponible=0""")
        return self.cursor.fetchall()

    # Listes des offres validées
    def offres_liste_validees(self):
        self.cursor.execute("""SELECT * FROM offres WHERE disponible=1""")
        return self.cursor.fetchall()

    # Récupération d'une offre
    def get_offre(self, offer_id):
        self.cursor.execute("""SELECT * FROM offres WHERE id = %s""", (offer_id,))
        return self.cursor.fetchall()

    # Listes des offres
    def offres_liste(self, page, mail):
        classe = self.get_user_info(mail)[0][3]
        offres = []
        self.cursor.execute(
            """SELECT * FROM offres WHERE disponible=1 AND (participant IS NULL OR participant2 IS NULL) LIMIT """ +
            str(offre_par_page) + """ OFFSET """ + str(page * offre_par_page))

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
        classe = self.get_user_info(mail)[0][3]
        offres = []
        self.cursor.execute(
            """SELECT * FROM offres WHERE disponible=1 ORDER BY """ + option + """ LIMIT """ +
            str(offre_par_page) + """ OFFSET """ + str(page * offre_par_page))

        rows = self.cursor.fetchall()
        # Tri des offres pour ne garder que celles où la classe du 1er participant est identique à celle de user
        for row in rows:
            if row[5] is None:
                offres.append(row)
            else:
                if classe == self.get_user_info(row[5])[0][3]:
                    offres.append(row)
        return offres

    # Liste des offres selon 1 facteur de tri + 1 niveau/matiere
    def offres_liste_tri_2(self, option, option2, page, mail):
        classe = self.get_user_info(mail)[0][3]
        offres = []
        self.cursor.execute(
            """SELECT * FROM offres WHERE disponible=1 AND (participant IS NULL OR participant2 IS NULL)
             AND """ + option + """ = '""" + option2 + """' LIMIT """ + str(offre_par_page) + """ OFFSET """ + str(
                page * offre_par_page))

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
        self.cursor.execute("""SELECT * FROM offres WHERE auteur = %s OR participant = %s OR participant2 = %s""",
                            (user_search, user_search, user_search))
        return self.cursor.fetchall()

    # Création d"une offre
    def create_offre(self, author, classe, matiere, horaires):
        date_time = datetime.datetime.now()
        date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute(
            """INSERT INTO offres (auteur, filiere, matiere, date_time) VALUES (%s, %s, %s, %s)""",
            (author, classe, matiere, date_time))

        i = 0
        for time in horaires:
            if time != 0:
                self.cursor.execute(
                    """UPDATE offres SET """ + horaires_reference[i] + """ = %s WHERE date_time = %s """,
                    (time, date_time))
            i += 1

        self.conn.commit()

    # Suppression d'une offre
    def delete_offer(self, offre_id):
        self.cursor.execute("""DELETE FROM offres WHERE id = %s""", (offre_id,))
        self.conn.commit()

    # Ajout de participant à une offre
    def add_participant(self, offre_id, participant):
        self.cursor.execute("""SELECT * FROM offres WHERE id=%s""", (offre_id,))
        offre = self.cursor.fetchall()[0]
        # Vérification auteur != participant
        if offre[1] != participant:
            if check_availability(offre) == 2:
                # Update de la première colonne
                self.cursor.execute("""UPDATE offres SET participant = %s WHERE id = %s """, (participant, offre_id))
                self.conn.commit()
                return 0
            elif check_availability(offre) == 1:
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
            return 3

    # Suppression d'un participant à une offre
    def delete_participant(self, offre_id, mail):
        self.cursor.execute("""SELECT * FROM offres WHERE id=%s""", (offre_id,))
        offres_a_modif = self.cursor.fetchall()
        if len(offres_a_modif) == 1:
            offre_a_modif = offres_a_modif[0]
            places_dispo = check_availability(offre_a_modif)
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

    """
        REQUETES DIVERSES SUR LA BDD
    """

    # SET CSS
    def set_css(self, mail):
        self.cursor.execute("""UPDATE users SET css = NOT css WHERE mail = %s""", (mail,))
        self.conn.commit()

    # GET CSS
    def get_css(self, mail):
        self.cursor.execute("""SELECT css FROM users WHERE mail = %s""", (mail,))
        if self.cursor.fetchall()[0][0] == 1:
            return True
        else:
            return False

    # Ban
    def ban(self, mail):
        self.cursor.execute("""UPDATE users SET ban = NOT ban WHERE mail = %s""", (mail,))
        self.conn.commit()

    # Modification du profil
    def modify_user_info(self, mail, classe):
        self.cursor.execute("""UPDATE users SET classe = %s WHERE mail = %s """,
                            (classe, mail))
        self.conn.commit()

    # Création d'un compte
    def create_compte(self, nom, mdp, mail, classe):
        self.cursor.execute(
            """INSERT INTO users (nom, mdp, mail, classe) VALUES (%s, %s, %s, %s)""",
            (nom, mdp, mail, classe))
        self.conn.commit()


# Retourne le nombre de places dispo
def check_availability(offre):
    if offre[5] is None or offre[6] is None:
        # Une place est disponible
        if offre[5] is None and offre[6] is None:
            return 2
        else:
            return 1
    else:
        return 0
