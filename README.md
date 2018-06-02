# BlaBla-Tutorat
**BlaBla-Tutorat** est une plateforme permettant de mettre en relation, au sein d'un établissement scolaire, des élèves ou étudiants souhaitant proposer ou recevoir de l'aide personnalisée.

> Ce programme a été réalisé dans le cadre du [projet d'ISN](http://info.blaisepascal.fr/blabla-tutorat) en 2018 par 3 élèves de terminale S.

#### Langages utilisés
* Python3
* SQL
* HTML
* CSS
* JS


## Installation
> L'installation de **BlaBla-Tutorat** est une opération réservée à l'administrateur d'un serveur de l'établissement.

### Prérequis
* Un serveur Python 3 (type Apache + wsgi)
* Un gestionnaire de base de données SQL

### Modules python3
* Flask
* mysql-connector

### Fichier de configuration
Un fichier de configuration, nommé `config.py`, comportant des données confidentielles doit être placé dans le répertoire du programme principal `index.py`.

Structure du fichier :
``` python
# coding: utf-8

host = "192.168.xxx.xxx"      # Adresse IP du serveur
user = "useruser"             # Nom d'utilisateur de la base de données
password = "mdpmdp"           # Mot de passe de la base de données
database = "tutorat"          # Nom de la base de données
secret_key = "clefsecrète"    # Clef secrète Flask (voir [Sessions Flask](http://flask.pocoo.org/docs/1.0/quickstart/#sessions))

# MAIL
smtp = "smtp.gmail.com"           # Nom du serveur smtp
smtp_port = 587                   # Port du serveur
email = "admintutorat@gmail.com"  # Adresse mail
email_password = "mdpmail"        # Mot de passe

# Identités et adresses email
webmaster = ({'nom': "nom_du_webmaster",  # Identité du webmaster
              'email': "email_du_webmaster"},)

developp = ({'nom': "Faury Cédrick",  # Identité des développeurs du site BlaBla-Tutorat
             'email': "cedrick.faury@ac-clermont.Fr"},
            {'nom': "Blancheton Tao",
             'email': "taotom63@gmail.com"},
            {'nom': "Desmoulins Marco",
             'email': "marco.desmoulins@lilo.org"},
            {'nom': "Labarussias Antoine",
             'email': "antoinelabarussias@orange.fr"})
```


#### Structure de la base de données
![Structure de la base de données](/images/Struct_Bdd.png)

## Contact
Utiliser le [gestionnaire de problèmes](https://github.com/BlaBlaTutorat/Tutorat/issues) de Github
