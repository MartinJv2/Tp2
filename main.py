"""
Ce code a ete ecrit pas Jeremy Martin.
Groupe : 403
le code fait en sorte que l`ordinateur joue un jeu de devinette avec le joueur
"""

from random import *

choix_du_joueur = int(input("L`ordinateur a choisit un nombre de 1 a 5.\n\n\t Essaye de le deviner!\n\n"))
choix_de_ordi = randint(1, 5)


def valeur_incorrecte_verification():  # verifie si la reponse donne par le joueur est correct.
    global choix_du_joueur

    if choix_du_joueur > choix_de_ordi:
        print("\tTa reponse est plus grande que celle de l`ordi\n\n")

    elif choix_du_joueur < choix_de_ordi:
        print("\tTa reponse est plus petite que celle de l`ordi\n\n")


def rejouer():  # verifie si le joueur peut rejouer. Si oui ca le demande de rejouer.
    global choix_de_ordi
    global choix_du_joueur

    if choix_du_joueur == choix_de_ordi:
        print("\tTa eu la reponse correct!!!\n\n")
        demande_de_rejouer = input("Recommencer? (non=1 oui=autre)\n\n")

        if demande_de_rejouer == "1":
            exit()

        else:
            choix_du_joueur = int(input("L`ordinateur a choisit un nombre de 1 a 5.\n\n Essaye de le deviner!\n\n"))
            choix_de_ordi = randint(1, 5)

    else:
        choix_du_joueur = int(input("\tRessayez\n\n"))


while True:
    valeur_incorrecte_verification()
    rejouer()
