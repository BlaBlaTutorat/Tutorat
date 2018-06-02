# coding: utf-8


class Offre:

    def __init__(self, sql):
        self.id = sql[0]
        self.auteur = sql[1]
        self.filiere = sql[2]
        self.matiere = sql[3]
        self.date_time = sql[4]
        self.participant = sql[5]
        self.participant2 = sql[6]
        self.dispo = sql[7]
        self.horaires = sql[8]


class Demande:

    def __init__(self, sql):
        self.id = sql[0]
        self.auteur = sql[1]
        self.classe = sql[2]
        self.matiere = sql[3]
        self.date_time = sql[4]
        self.tuteur = sql[5]
        self.dispo = sql[6]
        self.horaires = sql[7]


class Utilisateur:

    def __init__(self, sql):
        self.nom = sql[0]
        self.mdp = sql[1]
        self.mail = sql[2]
        self.classe = sql[3]
        self.ban = sql[4]
