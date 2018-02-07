import mysql.connector
import sys


class MysqlObject:

    # Méthode executée à la création de l'objet
    def __init__(self):

        try:

            self.conn = mysql.connector.connect("172.21.1.203", "isn", "0C5PH2iBfMy3l6o3", "tutorat")
            self.cursor = self.conn.cursor()

        except mysql.connector.errors.InterfaceError as e:

            print("Error %d: %s" % (e.args[0], e.args[1]))
            sys.exit(1)

    # Liste des niveaux
    def operation1(self):

        self.cursor.execute("""SELECT id,nom FROM niveaux""")

        rows = self.cursor.fetchall()
        for row in rows:
            print('Niveau {0}: {1}'.format(row[0], row[1]))

    # Méthode exécutée à la suppression de l'bbjet
    def __del__(self):
        self.cursor.close()
        self.conn.close()
