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

    # Listes des offres à valider
    def offres_liste_valider(self):
        self.cursor.execute("""SELECT * FROM offres WHERE disponible=0""")
        return self.cursor.fetchall()

    # Listes des offres validées
    def offres_liste_validees(self):
        self.cursor.execute("""SELECT * FROM offres WHERE disponible=1""")
        return self.cursor.fetchall()

    # Listes des utilisateurs
    def liste_user(self):
        self.cursor.execute("""SELECT * FROM users""")
        return self.cursor.fetchall()

    # Listes des offres
    def offres_liste(self, page, user):
        classe = self.get_user_info(user)[3]
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
                if classe == self.get_user_info(row[5])[3]:
                    offres.append(row)
        return offres

    # Liste des offres selon 1 facteur de tri
    def offres_liste_tri(self, option, page, user):
        classe = self.get_user_info(user)[3]
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
                if classe == self.get_user_info(row[5])[3]:
                    offres.append(row)
        return offres

    # Liste des offres selon 1 facteur de tri + 1 niveau/matiere
    def offres_liste_tri_2(self, option, option2, page, user):
        classe = self.get_user_info(user)[3]
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
                if classe == self.get_user_info(row[5])[3]:
                    offres.append(row)
        return offres

    # Récupération des infos utilisateurs pour page de profil
    def get_user_info(self, user_name):
        self.cursor.execute("""SELECT * FROM users WHERE nom=%s""", (user_name,))
        return self.cursor.fetchall()[0]
        
    #Connecter l'utilisateur
    def connect(self,mail, mdp_chiffre):
        self.cursor.execute("""Insert IN session""", (mail,mdp_chiffre))
        self.cursor.fetchall()[0]
        

    # Vérification que l'utilisateur est connecté
        
    def get_mail(self, mail):
        self.cursor.execute("""SELECT mail FROM users WHERE mail=%s""", (mail,))
        self.cursor.fetchall()


    # Récupération et cryptage du mot de passe des utilisateurs
    def get_crypt_mdp(self, mail):
        self.cursor.execute("""SELECT mdp FROM users WHERE mail=%s""", (mail,))
        return self.cursor.fetchall()

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
                    if self.get_user_info(participant)[3] == self.get_user_info(offre[5])[3]:
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

    # Récupération des offres propres à un utilisateur
    def get_user_offre(self, user_name):
        self.cursor.execute("""SELECT * FROM offres WHERE auteur=%s""", (user_name,))
        return self.cursor.fetchall()

    # Suppression d'une offre
    def delete_offer(self, offre_id):
        self.cursor.execute("""DELETE FROM offres WHERE id = %s""", (offre_id,))
        self.conn.commit()

    # Validation d'une offre
    def validate_offer(self, offre_id, disponible):
        self.cursor.execute("""UPDATE offres SET disponible = %s WHERE id = %s""", (disponible, offre_id))
        self.conn.commit()

    # SET CSS
    def set_css(self, user):
        self.cursor.execute("""UPDATE users SET css = NOT css WHERE nom = %s""", (user,))
        self.conn.commit()

    # GET CSS
    def get_css(self, user):
        self.cursor.execute("""SELECT css FROM users WHERE nom = %s""", (user,))
        if self.cursor.fetchall()[0][0] == 1:
            return True
        else:
            return False

    # Ban
    def ban(self, user_name):
        self.cursor.execute("""UPDATE users SET ban = NOT ban WHERE nom = %s""", (user_name,))
        self.conn.commit()

    # Modification du profil
    def modify_user_info(self, user_name, mail, classe):
        self.cursor.execute("""UPDATE users SET mail = %s, classe = %s WHERE nom = %s """,
                            (mail, classe, user_name))
        self.conn.commit()

    # Recherche des offres auxquelles participe l'utilisateur
    def get_user_tutorats(self, user_name):
        self.cursor.execute("""SELECT * FROM offres WHERE participant=%s OR participant2=%s""", (user_name, user_name))
        return self.cursor.fetchall()

    # Suppression d'un participant à une offre
    def delete_participant(self, offre_id, user):
        self.cursor.execute("""SELECT * FROM offres WHERE id=%s""", (offre_id,))
        offres_a_modif = self.cursor.fetchall()
        if len(offres_a_modif) == 1:
            offre_a_modif = offres_a_modif[0]
            places_dispo = check_availability(offre_a_modif)
            if places_dispo == 0:
                if offre_a_modif[5] == user:
                    self.cursor.execute(
                        """UPDATE offres SET participant = participant2, participant2 = NULL WHERE id = %s """,
                        (offre_id,))
                    self.conn.commit()
                    return True
                elif offre_a_modif[6] == user:
                    self.cursor.execute("""UPDATE offres SET participant2 = NULL WHERE id = %s """, (offre_id,))
                    self.conn.commit()
                    return True
                else:
                    # L'utilisateur ne participe pas au Tutorat
                    return False

            elif places_dispo == 1:
                if offre_a_modif[5] == user:
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

    # Création d'un compte
    def create_compte(self, nom, mdp, mail, classe):
        self.cursor.execute(
            """INSERT INTO users (nom, mdp, mail, classe) VALUES (%s, %s, %s, %s)""",
            (nom, mdp, mail, classe))
        self.conn.commit()

    # Méthode exécutée à la suppression de l'bbjet
    def __del__(self):
        self.cursor.close()
        self.conn.close()


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
