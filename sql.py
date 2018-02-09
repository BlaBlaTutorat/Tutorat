import mysql.connector
import sys


class MysqlObject:

    # Méthode executée à la création de l'objet
    def __init__(self):

        try:

            self.conn = mysql.connector.connect(host="172.21.1.203",
                                user="isn",
                                password="0C5PH2iBfMy3l6o3",
                                database="tutorat")
            self.cursor = self.conn.cursor()

        except mysql.connector.errors.InterfaceError as e:

            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

    # Liste des niveaux
    def operation1(self):
        l = []
        self.cursor.execute("""SELECT nom FROM niveaux ORDER BY id""")

        rows = self.cursor.fetchall()
        for row in rows:
            l.append(row[0])
        return l
        
    # Liste des matières
    def operation2(self):
        l = []
        self.cursor.execute("""SELECT * FROM matieres""")

        rows = self.cursor.fetchall()
        for row in rows:
            l.append(row[0])
        return l

    # Méthode exécutée à la suppression de l'bbjet
    def __del__(self):
        self.cursor.close()
        self.conn.close()
