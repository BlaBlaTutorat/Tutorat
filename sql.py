# coding: utf-8
import datetime
import sys
from operator import itemgetter

import mysql.connector

import config
import objects


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
		rows = sorted(self.cursor.fetchall(), key=itemgetter(1))
		# On ne retourne que le nom
		for row in rows:
			filieres.append(row[0])
		return filieres

	"""
		REQUETES CONCERNANT LES UTILISATEURS SUR LA BDD
	"""
	# Inscription intermédiaire
	def create_compte_validate(self, nom, mdp, mail, classe, code):
		"""Argument: Mail de l'utilisateur, nom, mot de passe, classe et le code de validation
		Fonction: Envoie les données à la BDD et crée un compte utilisateur intermédiaire"""
		self.cursor.execute(
			"""INSERT INTO register (nom, mdp, mail, classe, code) VALUES (%s, %s, %s, %s, %s)""",
			(nom, mdp, mail, classe, code))
		self.conn.commit()

	def code_update(self, code, mail):
		"""Argument: code de validation et mail
		Fonction: ajoute le bon code de validation d'inscription à la bdd"""
		self.cursor.execute("""UPDATE register SET code = %s WHERE mail = %s""", (code, mail))
		self.conn.commit()

	# Info pour l'inscription
	def info_register(self, mail):
		"""Renvoie les infos utilisateur pour l'inscription"""
		self.cursor.execute("""SELECT * FROM register WHERE mail=%s""", (mail,))
		return self.cursor.fetchall()

	# Suppression info inscription
	def delete_register(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: Supprime les infos d'inscription"""
		self.cursor.execute("""DELETE FROM register WHERE mail = %s""", (mail,))
		self.conn.commit()

	# Suppression de compte
	def delete_account(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: Supprime le compte utilisateur de la BDD et les offres et demandes créées par l'utilisateur"""
		self.cursor.execute("""DELETE FROM offres WHERE auteur = %s""", (mail,))
		self.cursor.execute("""DELETE FROM demandes WHERE auteur = %s""", (mail,))
		self.cursor.execute("""UPDATE offres SET participant = NULL WHERE participant = %s""", (mail,))
		self.cursor.execute("""UPDATE offres SET participant2 = NULL WHERE participant2 = %s""", (mail,))
		offres = self.get_all_offres()
		for offre in offres:
			if offre.participant is None and offre.participant2 is not None:
				participant = offre.participant2
				offre_id = offre.id
				self.cursor.execute("""UPDATE offres SET participant = %s WHERE id = %s""", (participant, offre_id))
				self.cursor.execute("""UPDATE offres SET participant2 = NULL WHERE id = %s""", (offre_id,))
		self.cursor.execute("""DELETE FROM users WHERE mail = %s""", (mail,))
		self.conn.commit()

	# Listes des utilisateurs
	def liste_user(self):
		"""Renvoie la liste des utilisateurs du site"""
		users = []
		self.cursor.execute("""SELECT * FROM users""")
		# Conversion en objet Utilisateur
		rows = self.cursor.fetchall()
		for row in rows:
			users.append(objects.Utilisateur(row))
		return users

	# Listes des responsables de suivi
	def liste_resp(self, codeFiliere):
		""" Renvoie la liste des responsable de suivi des élèves
			pour le code de filière donné (0 à 7)
		"""
		users = []
		self.cursor.execute("""SELECT * FROM users
								WHERE classe="ADMIN"
							""")
		# Conversion en objet Utilisateur
		rows = self.cursor.fetchall()
		for row in rows:
			# filtrage selon responsabilité
			u = objects.Utilisateur(row)
			if u.est_responsable_filiere(codeFiliere):
				users.append(u)
		return users

	# Vérifier si le mail existe
	def mail_in_bdd(self, mail):
		""" Argument: Mail de l'utilisateur
			Fonction: Vérifie si le mail existe
		"""
		self.cursor.execute("""SELECT mail FROM users WHERE mail =%s""", (mail,))
		if len(self.cursor.fetchall()) != 0:
			return True
		else:
			return False

	# Vérifier si le mail existe
	def mail_in_register(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: Vérifie si le mail existe"""
		self.cursor.execute("""SELECT mail FROM register WHERE mail =%s""", (mail,))
		if len(self.cursor.fetchall()) != 0:
			return True
		else:
			return False

	# Récupération des infos utilisateurs par mail
	def get_user_info(self, mail):
		""" Argument: Mail de l'utilisateur
			Fonction: Renvoie les données de l'utilisateur
		"""
		self.cursor.execute("""SELECT * FROM users WHERE mail=%s""", (mail,))
		# Conversion en objet Utilisateur
		return objects.Utilisateur(self.cursor.fetchall()[0])

	# Récupération des infos utilisateurs par pseudo ( ADMIN UNIQUEMENT )
	def get_user_info_pseudo(self, user_search):
		"""Argument: Pseudo de l'utilisateur
		Fonction: renvoie les données de l'utilisateur"""
		users = []
		self.cursor.execute("""SELECT * FROM users WHERE nom LIKE %s """, ("%{}%".format(user_search),))
		# Conversion en objet Utilisateur
		rows = self.cursor.fetchall()
		for row in rows:
			users.append(objects.Utilisateur(row))
		return users

	# Pseudo vers mail ( l'utilisateur existe )
	def get_user_mail(self, user):
		"""Argument: Pseudo de l'utilisateur
		Fonction: Renvoie le mail de l'utilisteur"""
		self.cursor.execute("""SELECT mail FROM users WHERE nom=%s""", (user,))
		return objects.Utilisateur(self.cursor.fetchall()[0]).nom

	# Check ban
	def check_ban(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: Vérifie si l'utilisateur est banni"""
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

	# Liste de toutes les offres
	def get_all_offres(self):
		offres = []
		self.cursor.execute("""SELECT * FROM offres""")
		# Conversion en objet Offre
		rows = self.cursor.fetchall()
		for row in rows:
			offres.append(objects.Offre(row))
		return offres

	# Liste offres utilisateur
	def get_user_offres(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: Renvoie la liste des offres créées par l'utilisateur"""
		offres = []
		self.cursor.execute(
			"""SELECT * FROM offres WHERE auteur=%s""", (mail,))
		# Conversion en objet Offre
		rows = self.cursor.fetchall()
		for row in rows:
			offres.append(objects.Offre(row))
		return offres

	# Recherche des offres auxquelles participe l'utilisateur
	def get_user_offres_suivies(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: Renvoie les offre auxquelles participe l'utilisateur"""
		offres = []
		self.cursor.execute("""SELECT * FROM offres WHERE participant=%s OR participant2=%s""", (mail, mail))
		# Conversion en objet Offre
		rows = self.cursor.fetchall()
		for row in rows:
			offres.append(objects.Offre(row))
		return offres

	# Listes des offres à valider
	def offres_liste_valider(self):
		"""Renvoie la liste des offres à valider"""
		offres = []
		self.cursor.execute("""SELECT * FROM offres WHERE disponible=0""")
		# Conversion en objet Offre
		rows = self.cursor.fetchall()
		for row in rows:
			offres.append(objects.Offre(row))
		return offres

	# Listes des offres validées
	def offres_liste_validees(self):
		"""Renvoie la liste des offres qui ont été validées"""
		offres = []
		self.cursor.execute("""SELECT * FROM offres WHERE disponible=1""")
		# Conversion en objet Offre
		rows = self.cursor.fetchall()
		for row in rows:
			offres.append(objects.Offre(row))
		return offres

	# Récupération d'une offre
	def get_offre(self, offer_id):
		"""Argument: Id de l'offre
		Fonction: Renvoie l'offre"""
		self.cursor.execute("""SELECT * FROM offres WHERE id = %s""", (offer_id,))
		# Conversion en objet Offre
		return objects.Offre(self.cursor.fetchall()[0])

	# Liste des offres compatibles avec l'utilisateur
	def liste_offres(self, mail, option=None, option2=None):
		"""Renvoie la liste des offres compatibles avec l'utilisateur connecté (même classe)
		
			:mail: adresse de l'utilisateur connecté
			:option: premier niveau de selection
			:option2: 2ème niveau de selection
		
		"""

		classe = self.get_user_info(mail).classe
		niveau = self.get_class_level(classe)
		offres = []

		if classe == "ADMIN":  # Administrateur !
			condition = "(1>0)"  # Tout !
		else:
			condition = "disponible=1 AND (participant IS NULL OR participant2 IS NULL)"

		if option is not None:
			if option == "relation":
				self.cursor.execute(
					"""SELECT * FROM offres WHERE participant is not NULL OR participant2 is not NULL""")
			elif option2 is not None:
				self.cursor.execute(
					"""SELECT * FROM offres WHERE """ + condition + """
					 AND """ + option + """ = '""" + option2 + "'")
			else:
				self.cursor.execute(
					"""SELECT * FROM offres WHERE """ + condition + """
					ORDER BY """ + option)
		else:
			self.cursor.execute("""SELECT * FROM offres WHERE """ + condition)

		rows = self.cursor.fetchall()
		# Tri des offres pour ne garder que celles où ...
		for row in rows:
			offre = objects.Offre(row)
			if classe == "ADMIN":  # Administrateur !
				offres.append(offre)
				continue

			if niveau <= self.get_filiere_level(offre.filiere):
				if offre.participant is None:  # ... les deux places sont disponibles
					offres.append(offre)
				else:
					if mail == offre.participant:  # ... l'utilisateur est déjà inscrit
						continue
					if classe == self.get_user_info(
							offre.participant).classe:  # ... la classe du 1er participant est identique à celle de user
						offres.append(offre)

		return offres

	# Listes des offres tri admin
	def offres_liste_tri_admin(self, user_search):
		"""Argument: Mail de l'utilisateur
		Fonction: Renvoie la liste des offres quand on recherche un utilisateur"""
		offres = []
		self.cursor.execute(
			"""SELECT * FROM offres WHERE auteur = %s OR participant = %s OR participant2 = %s AND disponible=1""",
			(user_search, user_search, user_search))
		# Conversion en objet Offre
		rows = self.cursor.fetchall()
		for row in rows:
			offres.append(objects.Offre(row))
		return offres

	# Création d"une offre
	def create_offre(self, author, classe, matiere, horaires):
		""" Argument: Mail de l'utilisateur, Filière, matière, horaires
			Fonction: Envoie les infos à la BDD et crée l'offre
			et notifie les responsables 
		"""
		date_time = datetime.datetime.now()
		date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
		
		self.cursor.execute(
			"""INSERT INTO offres (auteur, filiere, matiere, date_time, horaires) VALUES (%s, %s, %s, %s, %s)""",
			(author, classe, matiere, date_time, horaires))
		self.conn.commit()
		
		
		# Notification
		c = self.get_user_info(author)
		for u in self.liste_resp(self.get_filiere_level(classe)):
			u.notifier("Nouvelle offre",
					   "L'utilisateur suivant :\n %s\n, vient de déposer l'offre suivante :\n" \
					   "  Filière : %s\n" \
					   "  Matière : %s\n" \
					   "\nCette offre doit à présent être validée.\n" \
					   "" %(c.get_profil_texte(), classe, matiere))

	# Suppression d'une offre
	def delete_offer(self, offre_id):
		"""Argument: Id de l'offre
		Fonction: Surpime l'offre"""
		self.cursor.execute("""DELETE FROM offres WHERE id = %s""", (offre_id,))
		self.conn.commit()

	# Ajout de participant à une offre
	def add_participant(self, offre_id, participant):
		""" Argument: Id de l'offre, mail du participant
			Fonction: Ajoute un participant à une offre
		"""
		def notify(offre):
			# Notification
			c = self.get_user_info(participant)
			for u in self.liste_resp(self.get_filiere_level(offre.filiere)):
				u.notifier("Offre acceptée",
						   "L'utilisateur suivant :\n%s\n\n" \
						   "vient d'accepter l'offre suivante :\n%s\n" \
						   "\nLes deux utilisateurs doivent être mis en contact.\n" \
						   "" %(c.get_profil_texte(), offre.get_texte()))
					   
					   
		self.cursor.execute("""SELECT * FROM offres WHERE id=%s""", (offre_id,))
		offre = objects.Offre(self.cursor.fetchall()[0])
		if offre.auteur != participant:
			if self.places(offre.id) == 2:
				# Update de la première colonne
				self.cursor.execute("""UPDATE offres SET participant = %s WHERE id = %s """, (participant, offre_id))
				self.conn.commit()
				notify(offre)
				return 0
			elif self.places(offre.id) == 1:
				# Update de la deuxième colonne + check si l'utilisateur n'est pas déjà participant à cette offre
				if offre.participant != participant:
					# Check si l'utilisateur est dans la même classe que le premier
					if self.get_user_info(participant).classe == self.get_user_info(offre.participant).classe:
						self.cursor.execute("""UPDATE offres SET participant2 = %s WHERE id = %s """,
											(participant, offre_id))
						self.conn.commit()
						notify(offre)
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
		Fonction: Supprime le participant de l'offre"""
		self.cursor.execute("""SELECT * FROM offres WHERE id=%s""", (offre_id,))
		offres_a_modif = self.cursor.fetchall()
		if len(offres_a_modif) == 1:
			offre_a_modif = objects.Offre(offres_a_modif[0])
			places_dispo = self.places(offre_a_modif.id)
			if places_dispo == 0:
				if offre_a_modif.participant == mail:
					self.cursor.execute(
						"""UPDATE offres SET participant = participant2, participant2 = NULL WHERE id = %s """,
						(offre_id,))
					self.conn.commit()
					return True
				elif offre_a_modif.participant2 == mail:
					self.cursor.execute("""UPDATE offres SET participant2 = NULL WHERE id = %s """, (offre_id,))
					self.conn.commit()
					return True
				else:
					# L'utilisateur ne participe pas au Tutorat
					return False
			elif places_dispo == 1:
				if offre_a_modif.participant == mail:
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
	def modifier_offre(self, mail, offre_id, horaires):
		self.cursor.execute("""UPDATE offres SET horaires = %s WHERE id = %s""", (horaires, offre_id))
		self.conn.commit()


	# mail in offre ?
	def mail_in_offre(self, id_o, mail):
		self.cursor.execute("""SELECT * FROM offres where id = %s""", (id_o,))

		offre = objects.Offre(self.cursor.fetchall()[0])
		participants = [offre.participant, offre.participant2]

		if mail in participants:
			return True
		else:
			return False

	"""
		REQUETES DIVERSES SUR LA BDD
	"""

	# Ban
	def ban(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: Bannir l'utilisateur"""
		self.cursor.execute("""UPDATE users SET ban = NOT ban WHERE mail = %s""", (mail,))
		self.cursor.execute("""DELETE FROM offres WHERE auteur = %s""", (mail,))
		self.cursor.execute("""DELETE FROM demandes WHERE auteur = %s""", (mail,))
		self.cursor.execute("""UPDATE offres SET participant = NULL WHERE participant = %s""", (mail,))
		self.cursor.execute("""UPDATE offres SET participant2 = NULL WHERE participant2 = %s""", (mail,))
		offres = self.get_all_offres()
		for offre in offres:
			if offre.participant is None and offre.participant2 is not None:
				participant = offre.participant2
				offre_id = offre.id
				self.cursor.execute("""UPDATE offres SET participant = %s WHERE id = %s""", (participant, offre_id))
				self.cursor.execute("""UPDATE offres SET participant2 = NULL WHERE id = %s""", (offre_id,))
		self.conn.commit()

	# Promouvoir
	def promote(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: promouvoir un utilisateur en administrateur"""
		self.cursor.execute("""UPDATE users SET classe = 'ADMIN' WHERE mail = %s""", (mail,))
		self.conn.commit()

	# Rétrograder
	def retrograder(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: retrograder un administrateur en utilisateur"""
		self.cursor.execute("""UPDATE users SET classe = %s WHERE mail = %s""", ("1ES1", mail))
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
		""" Argument: Mail de l'utilisateur, nom, mot de passe, classe
			Fonction: Envoie les données à la BDD et crée un compte utilisateur
		"""
		self.cursor.execute(
			"""INSERT INTO users (nom, mdp, mail, classe) VALUES (%s, %s, %s, %s)""", (nom, mdp, mail, classe))
		self.conn.commit()
		
		# Notification
		c = self.get_user_info(mail)
		for u in self.liste_resp(self.get_filiere_level(classe)):
			u.notifier("Nouvel inscrit",
					   "Un nouvel utilisateur vient de s'insrire sur le site :" \
					   "  Filière : %s\n" \
					   "  Matière : %s\n" \
					   "" %(c.get_profil_texte()))
					   
					   

	# Reset
	def reset(self):
		"""Remet le site a 0"""
		self.cursor.execute("""DELETE FROM `users` WHERE classe != 'ADMIN'""")
		self.cursor.execute("""DELETE FROM `offres`""")
		self.cursor.execute("""DELETE FROM `demandes`""")
		self.cursor.execute("""DELETE FROM `register`""")
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
		Fonction: Supprime l'offre"""
		self.cursor.execute("""DELETE FROM demandes WHERE id = %s""", (demande_id,))
		self.conn.commit()

	# Création d'une demande
	def create_demande(self, author, classe, matiere, horaires):
		""" Argument: Mail de l'auteur, Filière, Matière, Horaires
			Fonction: Envoie les infos à la BDD et crée la demande
		"""
		date_time = datetime.datetime.now()
		date_time = date_time.strftime("%Y-%m-%d %H:%M:%S")
		self.cursor.execute(
			"""INSERT INTO demandes (auteur, classe, matiere, date_time, horaires) VALUES (%s, %s, %s, %s, %s)""",
			(author, classe, matiere, date_time, horaires))
		self.conn.commit()
		
		# Notification
		c = self.get_user_info(author)
		for u in self.liste_resp(self.get_filiere_level(classe)):
			u.notifier("Nouvelle offre",
					   "L'utilisateur %s, vient de déposer la demande suivante : \n" \
					   "  Filière : %s\n" \
					   "  Matière : %s\n" \
					   "Cette offre doit à présent être validée.\n" \
					   "" %(c.get_profil_texte(), classe, matiere))
					   
					   

	# Récupération d'une demande
	def get_demande(self, demande_id):
		"""Argument: Id de la demande
		Fonction: Renvoie la demande"""
		self.cursor.execute("""SELECT * FROM demandes WHERE id = %s""", (demande_id,))
		# Conversion en objet Demande
		return objects.Demande(self.cursor.fetchall()[0])

	# Liste des offres compatibles avec l'utilisateur
	def liste_demandes(self, mail, option = None, option2 = None):
		"""Renvoie la liste des demandes compatibles avec l'utilisateur connecté (classe inférieure)
		
			:mail: adresse de l'utilisateur connecté
			:option: premier niveau de selection
			:option2: 2ème niveau de selection
		
		"""
		classe = self.get_user_info(mail).classe
		niveau = self.get_class_level(classe)
		demandes = []

		if classe == "ADMIN":  # Administrateur !
			condition = "(1>0)"  # Tout !
		else:
			condition = "disponible=1 AND tuteur IS NULL"


		if option is not None:
			if option == "relation":
				self.cursor.execute(
					"""SELECT * FROM demandes WHERE tuteur is not NULL""")
			elif option2 is not None:
				self.cursor.execute(
					"""SELECT * FROM demandes WHERE """ + condition + """
					 AND """ + option + """ = '""" + option2 + """'""")
			else:
				self.cursor.execute(
					"""SELECT * FROM demandes WHERE """ + condition + """
					ORDER BY """ + option)
		else:
			self.cursor.execute(
				"""SELECT * FROM demandes WHERE """ + condition)

		rows = self.cursor.fetchall()

		# Tri des demandes pour ne garder que celles où le niveau de l'utilisateur est supérieur au niveau de la demande
		for row in rows:
			demande = objects.Demande(row)
#			 demande.SetNomTuteur(self.cursor)
			
			if classe == "ADMIN":  # Administrateur !
				demandes.append(demande)
				continue

			if niveau >= self.get_class_level(demande.classe):
				demandes.append(demande)
		return demandes

	# Liste des matières/filieres parmis les offres/demandes disponibles
	def liste_dispo(self, colonne, table, admin):
		""" Renvoie la liste des matières parmi les offres/demandes disponibles
			:colonne: 'matiere' ou 'filiere'
			:table: type d'élément : 'offres' ou 'demandes'
		"""

		if admin:
			self.cursor.execute("""SELECT DISTINCT """ + colonne + """ FROM """ + table)
		else:
			if table == 'demandes':
				self.cursor.execute(
					"""SELECT DISTINCT """ + colonne + """ FROM demandes WHERE disponible=1 AND tuteur IS NULL""")
			elif table == 'offres':
				self.cursor.execute(
					"""SELECT DISTINCT """ + colonne + """ FROM offres WHERE disponible=1 AND (participant IS NULL
					 OR participant2 IS NULL)""")

		mat = self.cursor.fetchall()
		mat = [m[0] for m in mat]
		return mat

	# Liste demandes utilisateur
	def get_user_demandes(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: Renvoie la liste des demandes créées par l'utilisateur"""
		demandes = []
		self.cursor.execute(
			"""SELECT * FROM demandes WHERE auteur=%s""", (mail,))
		# Conversion en objet Demande
		rows = self.cursor.fetchall()
		for row in rows:
			demandes.append(objects.Demande(row))
		return demandes

	# Liste demandes utilisateur
	def get_user_demandes_tuteur(self, mail):
		"""Argument: Mail de l'utilisateur
		Fonction: Renvoie la liste des demandes où l'utilisateur est le tuteur"""
		demandes = []
		self.cursor.execute(
			"""SELECT * FROM demandes WHERE tuteur=%s""", (mail,))
		# Conversion en objet Demande
		rows = self.cursor.fetchall()
		for row in rows:
			demandes.append(objects.Demande(row))
		return demandes

	# Listes des demandes à valider
	def demandes_liste_valider(self):
		"""Renvoie la liste des demandes à valider"""
		demandes = []
		self.cursor.execute("""SELECT * FROM demandes WHERE disponible=0""")
		# Conversion en objet Demande
		rows = self.cursor.fetchall()
		for row in rows:
			demandes.append(objects.Demande(row))
		return demandes

	# Quitter une demande
	def quit_demande(self, id_d, mail):
		"""Quitte la demande"""
		self.cursor.execute("""UPDATE demandes SET tuteur = NULL WHERE id = %s AND tuteur = %s""", (id_d, mail,))
		self.conn.commit()

	# Listes des demandes validées
	def demandes_liste_validees(self):
		"""Renvoie la liste des demandes qui ont été validées"""
		demandes = []
		self.cursor.execute("""SELECT * FROM demandes WHERE disponible=1""")
		# Conversion en objet Demande
		rows = self.cursor.fetchall()
		for row in rows:
			demandes.append(objects.Demande(row))
		return demandes

	# Validation d'une demande
	def validate_demande(self, demande_id, disponible):
		"""Argument: id de la demande, disponible
		Fonction: Valide une demande"""
		self.cursor.execute("""UPDATE demandes SET disponible = %s WHERE id = %s""", (disponible, demande_id))
		self.conn.commit()

	# Listes des offres tri admin
	def demandes_liste_tri_admin(self, user_search):
		"""Argument: Mail de l'utilisateur
		Fonction: Renvoie la liste des demande en fonction de l'utilisateur recherché"""
		demandes = []
		self.cursor.execute(
			"""SELECT * FROM demandes WHERE auteur = %s OR tuteur = %s AND disponible=1""",
			(user_search, user_search))
		# Conversion en objet Demande
		rows = self.cursor.fetchall()
		for row in rows:
			demandes.append(objects.Demande(row))
		return demandes

	# Ajout tuteur à une demande
	def add_tuteur(self, demande_id, mail):
		""" Argument: id de la demande, mail de l'utilisateur
			Fonction: Ajoute un tuteur a la demande
		"""
		def notify(demande):
			# Notification
			c = self.get_user_info(mail)
			for u in self.liste_resp(self.get_classe_level(demande.classe)):
				u.notifier("Demande acceptée",
						   "L'utilisateur suivant :\n%s\n\n" \
						   "vient d'accepter la demande suivante :\n%s\n" \
						   "\nLes deux utilisateurs doivent être mis en contact.\n" \
						   "" %(c.get_profil_texte(), demande.get_texte()))
						   
						   
		self.cursor.execute("""SELECT * FROM demandes WHERE id=%s""", (demande_id,))
		demande = objects.Demande(self.cursor.fetchall()[0])
		if demande.auteur != mail:
			if demande.tuteur is None:
				# Update de la première colonne
				self.cursor.execute("""UPDATE demandes SET tuteur = %s WHERE id = %s """, (mail, demande_id))
				self.conn.commit()
				notify(demande)
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

	# Liste des demandes
	def get_all_demandes(self):
		demandes = []
		self.cursor.execute("""SELECT * FROM demandes""")
		# Conversion en objet Demande
		rows = self.cursor.fetchall()
		for row in rows:
			demandes.append(objects.Demande(row))
		return demandes

	# Niveau classe
	def get_class_level(self, classe):
		self.cursor.execute("""SELECT classement FROM classes WHERE NOM = %s""", (classe,))
		lvl = self.cursor.fetchall()
		if len(lvl) > 0:
			lvl = lvl[0]
			if type(lvl) != int:
				lvl = lvl[0]
			return lvl

	# Niveau filière
	def get_filiere_level(self, filiere):
		self.cursor.execute("""SELECT classement FROM filieres
								WHERE nom = %s""", (filiere,))
		lvl_o = self.cursor.fetchall()
		if len(lvl_o) > 0:
			lvl_o = lvl_o[0]
			if type(lvl_o) != int:
				lvl_o = lvl_o[0]
			return lvl_o
			
	# Liste des filières
	def get_liste_filiere(self, lst_codes):
		""" Renvoie la liste des noms de filières
			à partir de la liste de leurs codes (ex : [1,5,6])
		"""
		#lst_codes = ",".join([str(n) for n in lst_codes])
		if len(lst_codes) == 0:
			return []
		format_strings = ','.join(['%s'] * len(lst_codes))
		
		self.cursor.execute("""SELECT nom FROM filieres
								WHERE classement IN (%s)
								ORDER BY classement, nom""" %format_strings, 
								tuple(lst_codes))
		l = self.cursor.fetchall()
		print(l)
		if len(l) > 0:
			return [n[0] for n in l]
		else:
			return []

	# Filière à partir du niveau
	def get_nom_niveau(self, niveau):
		nn = ["Seconde", "Première", "Terminale", "CPGE 1", "CPGE 2"]
		return nn[niveau]
	
#	 # Filière d'une classe
#	 def get_filiere_classe(self, classe):
#		 level = self.get_class_level(classe)
#		 self.cursor.execute("""SELECT nom FROM filieres WHERE classement = %s""", (level,))
#		 lst_filieres = self.cursor.fetchall()
#		 if len(lst_filieres) == 1:
#			 return lst_filieres[0]
#		 if level == 1 or level == 2: # premère ou terminale
#			 lst_filieres=[f for f in lst_filieres if f.split()[1] in classe]
#		 
#		 return
	
	
	# Demande a-t-elle un tuteur ?
	def demande_tuteur(self, id_d):
		self.cursor.execute("""SELECT * FROM demandes WHERE id=%s""", (id_d,))
		if objects.Demande(self.cursor.fetchall()[0]).tuteur is not None:
			tuteur = 1
		else:
			tuteur = 0
		return tuteur

	# Nombre de places dispo dans une offre
	def places(self, id_o):
		self.cursor.execute("""SELECT * FROM offres WHERE id=%s""", (id_o,))

		offre = objects.Offre(self.cursor.fetchall()[0])

		if offre.participant is None or offre.participant2 is None:
			# Une place est disponible
			if offre.participant is None and offre.participant2 is None:
				return 2
			else:
				return 1
		else:
			return 0

	# Mail in demande ?
	def mail_in_demande(self, id_d, mail):
		self.cursor.execute("""SELECT * FROM demandes where id = %s""", (id_d,))
		tuteur = objects.Demande(self.cursor.fetchall()[0]).tuteur
		if tuteur == mail:
			return True
		else:
			return False

	"""
		SUGGESTIONS
	"""

	# Offres
	def get_tutore_info(self, mail):
		demandes = self.get_user_demandes(mail)

		# liste des suggestions de niveau 1 :
		suggest_d1 = []
		# Liste des suggestions de niveau 2 :
		suggest_d2 = []

		for demande in demandes:

			# variable demandes :
			lvl = self.get_class_level(demande.classe)

			offres = self.get_all_offres()

			for offre in offres:

				# variable offres :
				lvl_o = self.get_filiere_level(offre.filiere)

				if lvl_o >= lvl and demande.matiere == offre.matiere and self.demande_tuteur(demande.id) == 0:
					if self.places(offre.id) > 0 and self.mail_in_offre(offre.id, mail) is False:
						if self.mail_in_demande(demande.id, mail) is False:
							suggest_d1.append(offre)
							n = 0
							for i in range(132):
								if int(demande.horaires[i]) == 1 and int(offre.horaires[i]) == 1:
									n += 1

							if n >= 1:
								suggest_d2.append(offre)
								del suggest_d1[-1]

		suggest = [suggest_d1, suggest_d2]
		return suggest

	# Demandes
	def get_tuteur_info(self, mail):
		offres = self.get_user_offres(mail)

		# liste des suggestions de niveau 1 :
		suggest_o1 = []
		# Liste des suggestions de niveau 2 :
		suggest_o2 = []

		for offre in offres:

			# variable offres :
			lvl = self.get_filiere_level(offre.filiere)

			demandes = self.get_all_demandes()

			for demande in demandes:

				# variable demandes :
				lvl_d = self.get_class_level(demande.classe)

				if lvl_d >= lvl and offre.matiere == demande.matiere and self.demande_tuteur(demande.id) == 0:
					if self.places(offre.id) > 0 and self.mail_in_demande(demande.id, mail) is False:
						if self.mail_in_offre(offre.id, mail) is False:
							suggest_o1.append(demande)
							n = 0
							for i in range(132):
								if int(offre.horaires[i]) == 1 and int(demande.horaires[i]) == 1:
									n += 1

							if n >= 1:
								suggest_o2.append(demande)
								del suggest_o1[-1]

		suggest = [suggest_o1, suggest_o2]
		return suggest
