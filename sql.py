import mysql.connector
import sys
import datetime

horaires_reference = ["debut_j1", "fin_j1", "debut_j2", "fin_j2", "debut_j3", "fin_j3", "debut_j4", "fin_j4",
                      "debut_j5",
                      "fin_j5", "debut_j6", "fin_j6"]


class MysqlObject:

    # Méthode executée à la création de l'objet
    def __init__(self):

        try:

            # self.conn = mysql.connector.connect(host="172.21.1.203", user="isn", password="0C5PH2iBfMy3l6o3",
            #                                    database="tutorat")
            self.conn = mysql.connector.connect(host="127.0.0.1", user="root", password="",
                                                database="tutorat")
            self.cursor = self.conn.cursor()

        except mysql.connector.errors.InterfaceError as e:

            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)
            
    # Liste des filieres
    def filieres_liste(self):
        filieres = []
        self.cursor.execute("""SELECT nom FROM filieres ORDER BY id""")

        rows = self.cursor.fetchall()
        for row in rows:
            filieres.append(row[0])
        return filieres
      
    # Liste des niveaux
    def niveaux_liste(self):
        niveaux = []
        self.cursor.execute("""SELECT nom FROM niveaux ORDER BY id""")

        rows = self.cursor.fetchall()
        for row in rows:
            niveaux.append(row[0])
        return niveaux

    # Liste des matières
    def matieres_liste(self):
        matieres = []
        self.cursor.execute("""SELECT * FROM matieres""")

        rows = self.cursor.fetchall()
        for row in rows:
            matieres.append(row[0])
        return matieres

    # Listes des offres
    def offres_liste(self):
        self.cursor.execute("""SELECT * FROM offres WHERE disponible=1""")
        return self.cursor.fetchall()

    # Création d"une offre
    def create_offre(self, author, niveau, matiere, horaires):
        date_time = datetime.datetime.now()
        date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
        self.cursor.execute("""INSERT INTO offres (auteur, niveau, matiere, date_time) VALUES (%s, %s, %s, %s)""",
                            (author,
                             niveau,
                             matiere,
                             date_time))

        i = 0
        for time in horaires:
            if time != 0:
                self.cursor.execute(
                    """UPDATE offres SET """ + horaires_reference[i] + """ = %s WHERE date_time = %s """,
                    (time, date_time))
            i += 1

        self.conn.commit()

    # Liste des offres selon 1 facteur de tri
    def offres_liste_tri(self, option):
        if option == "niveau":
            # Procédure spéciale pour les niveaux pour avoir un tri cohérent
            self.cursor.execute(
                """SELECT * FROM offres WHERE disponible=1 ORDER BY CASE """ + option + """ WHEN 'Seconde'
                 THEN 1 WHEN 'Première' THEN 2 WHEN 'Terminale' THEN 3 WHEN 'CPGE première année' 
                 THEN 4 WHEN 'CPGE deuxième année' THEN 5 END""")
        else:
            self.cursor.execute("""SELECT * FROM offres WHERE disponible=1 ORDER BY """ + option)
        return self.cursor.fetchall()

    # Liste des offres selon 1 facteur de tri + 1 niveau/matiere préférée
    def offres_liste_tri_2(self, option, option2):
        self.cursor.execute('SELECT * FROM offres WHERE disponible=1 ORDER BY CASE ' + option + ' WHEN "' + option2 +
                            '" THEN 1 ELSE ' + option + ' END')

        return self.cursor.fetchall()

    def get_user_info(self, name):
        self.cursor.execute("""SELECT * FROM users WHERE nom=%s""", (name,))
        return self.cursor.fetchall()

    # Méthode exécutée à la suppression de l'bbjet
    def __del__(self):
        self.cursor.close()
        self.conn.close()
