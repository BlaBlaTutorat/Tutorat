# coding: utf-8
# Fichier contenant toutes les fonctions simples utilisées dans les autres fichiers


# Retourne le nombre de places dispo en fonction d'une offre
def check_availability(offre):
    if offre.participant is None or offre.participant2 is None:
        # Une place est disponible
        if offre.participant is None and offre.participant2 is None:
            return 2
        else:
            return 1
    else:
        return 0
