import mysql.connector
import sys


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

    def offres_liste(self):
        self.cursor.execute("""SELECT * FROM offres""")
        return self.cursor.fetchall()

    # Méthode exécutée à la suppression de l'bbjet
    def __del__(self):
        self.cursor.close()
        self.conn.close()
