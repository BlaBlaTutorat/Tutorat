# coding: utf-8
# Fichier contenant toutes les fonctions simples utilisées dans les autres fichiers


# Retourne le nombre de places dispo en fonction d'une offre
def check_availability(offre):
    if offre[5] is None or offre[6] is None:
        # Une place est disponible
        if offre[5] is None and offre[6] is None:
            return 2
        else:
            return 1
    else:
        return 0
