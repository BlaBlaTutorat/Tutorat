# coding: utf-8
import config
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sql

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
	
	def get_texte(self):
		""" Renvoie les détails de l'offre sous forme de texte
		"""
		return "  Auteur : %s\n" \
			   "  Filière : %s\n" \
			   "  Matière : %s\n" \
			   "  Participants :\n" \
			   "    %s\n" \
			   "    %s\n" \
				%(self.auteur , self.filiere, 
				  self.matiere, self.participant, self.participant2)


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
		self.nomTuteur = ""
	
	def get_texte(self):
		""" Renvoie les détails de l'offre sous forme de texte
		"""
		return "  Auteur : %s\n" \
			   "  Classe :%s\n" \
			   "  Matière : %s\n" \
			   "  Tuteur : %s\n" \
				%(self.auteur , self.classe, self.matiere, self.tuteur)


	def SetNomTuteur(self, cursor):
		cursor.execute(
			"""SELECT * FROM users WHERE mail=""" + self.tuteur)
		lu = cursor.fetchall()
		if len(lu)>0:
			self.nomTuteur = Utilisateur(lu[0]).nom
				

class Utilisateur:
	def __init__(self, sql):
		self.nom = sql[0]
		self.mdp = sql[1]
		self.mail = sql[2]
		self.classe = sql[3]
		self.ban = sql[4]
		self.responsable = sql[5]
		
	def get_list_responsabilite(self):
		""" Renvoi la liste des classements de filière
			dont l'utilisateur est responsable du suivi
		"""
		l = list(bin(self.responsable)[:1:-1])
		return [i for i, n in enumerate(l) if n=="1"]
	
	
	def get_list_responsabilite_texte(self):
		""" Renvoi la liste des classements de filière
			dont l'utilisateur est responsable du suivi
		"""
		sql_obj = sql.MysqlObject()
		l = self.get_list_responsabilite()
		print(self.nom, "\n", l)
		l = sql_obj.get_liste_filiere(l)
		#print(self.nom, "\n")
		return l
	
	
	def add_responsabilite(self, code):
		""" Ajoute la responsabilité d'une filière
			de code donné (0 à 7)
		"""
		if not self.est_responsable_filiere(code):
			self.responsable += 2**code

	def sup_responsabilite(self, code):
		""" Retire la responsabilité d'une filière
			de code donné (0 à 7)
		"""
		if self.est_responsable_filiere(code):
			self.responsable -= 2**code

	def est_responsable_filiere(self, code):
		""" Renvoie True si l'utilisateur est responsable
			de la filière de code donné (0 à 7)
		"""
		return self.responsable & (2**code)
		
	def notifier(self, sujet, message):
		""" Envoi d'un e-mail de notification
		"""
		msg = MIMEMultipart()
		msg['From'] = config.email
		msg['To'] = self.mail
		msg['Subject'] = "BlaBla-Tutorat -- "+sujet
		msg.attach(MIMEText(message))
		mailserver = smtplib.SMTP(config.smtp, config.smtp_port)
		mailserver.starttls()
		mailserver.login(config.email, config.email_password)
		mailserver.sendmail(msg['From'], msg['To'], msg.as_string())
		mailserver.quit()

	def get_profil_texte(self):
		""" Renvoie le profil de l'utilisateur sous forme de texte
		"""
		return "  Nom : %s\n" \
			   "  e_mail : %s\n" \
			   "  Classe : %s" \
			   %(self.nom , self.mail, self.classe)


		
		
