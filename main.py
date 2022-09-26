"""
Ce code a ete ecrit pas Jeremy Martin
Groupe : 403
le code fait en sorte que l`ordinateur joue un jeu de devinette avec le joueur
"""

from random import *
choix_du_joueur = int(input("L`ordinateur a choisit un nombre de 1 a 10000.\n Essaye de le deviner!"))
choix_de_ordi=randint(1,5)


def valeur_incorrecte_verification():
    global choix_du_joueur
    if choix_du_joueur !=choix_de_ordi:
        if choix_du_joueur > choix_de_ordi:
            print("Ta reponse est plus grande que celle de l`ordi")
        elif choix_du_joueur < choix_de_ordi:
            print("Ta reponse est plus petite que celle de l`ordi")
        elif choix_du_joueur < choix_de_ordi:
            print("Ta eu la reponse correct!!!")
            reponse_correct=True


while True:
    reponse_correct = False
    valeur_incorrecte_verification()
    if reponse_correct==True:
        demande_de_rejouer=input("Recommencer? (non=1 oui=autre)")
        if demande_de_rejouer==("1"):
            exit()
        else:
            break
    else:
        choix_du_joueur=int(input("Essayez de nouveau"))

