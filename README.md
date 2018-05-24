# BlaBla-Tutorat
**BlaBla-Tutorat** est une plateforme permettant de mettre en relation, au sein d'un établissement scolaire, des élèves ou étudiants souhaitant proposer ou recevoir de l'aide personnalisée.

> Ce programme a éé réalisé dans le cadre du [projet d'ISN](http://info.blaisepascal.fr/blabla-tutorat) en 2018 par 3 élèves de terminale S.

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
Un fichier de configuration, nommé config.py, comportant des données confidentielles doit être placé dans le répertoire du programme principal index.py.

Structure du fichier :
``` python
# coding: utf-8

host = "192.168.xxx.xxx"      # Adresse IP du serveur
user = "useruser"             # Nom d'utilisateur de la base de données
password = "mdpmdp"           # Mot de passe
database = "tutorat"          # Nom de la base de données

# MAIL
smtp = "smtp.gmail.com"           # Nom du serveur smtp
smtp_port = 587                   # Port du serveur
email = "admintutorat@gmail.com"  # Adresse mail
email_password = "mdpmail"        # Mot de passe
```


#### Structure de la base de données
![Structure de la base de données](/images/Struct_Bdd.png)

## Contact
Utiliser le [gestionnaire de problèmes](https://github.com/BlaBlaTutorat/Tutorat/issues) de Github
