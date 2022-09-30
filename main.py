"""
Ce code a ete ecrit pas Jeremy Martin.
Groupe : 403
le code fait en sorte que l`ordinateur joue un jeu de devinette avec le joueur
"""

from random import randint
essaies = 0

minimum = int(input("Entrez le plus petit nombre que l`ordi peut choisir"))
maximum = int(input("Entrez le plus grand nombre que l`ordi peut choisir"))
print("L`ordi a un nombre de ", minimum, " a", maximum, ".\n\n\t Essaye de le deviner!\n\n")
choix_du_joueur, choix_de_ordi = int(input()), randint(minimum, maximum)


def valeur_incorrecte_verification():
    """
    verifie si la reponse donne par le joueur est correct.
    :return:
    """

    if choix_du_joueur > choix_de_ordi:
        print("\tTa reponse est plus grande que celle de l`ordi\n\n")
    elif choix_du_joueur < choix_de_ordi:
        print("\tTa reponse est plus petite que celle de l`ordi\n\n")


def rejouer():
    """
    verifie si le joueur peut rejouer. Si oui, ca le demande de rejouer.
    :return:
    """
    global choix_de_ordi, essaies, choix_du_joueur

    essaies += 1
    if choix_du_joueur == choix_de_ordi:
        print("\tTa eu la reponse correct!!! (", essaies, "essaies)\n\n")
        demande_de_rejouer = input("Recommencer? (non=1 oui=autre)\n\n")
        if demande_de_rejouer == "1":
            exit()
        else:
            minimum, maximum = int(input("Entrez le plus petit nombre que l`ordi peut choisir")), int(
                input("Entrez le plus grand nombre que l`ordi peut choisir"))
            print("L`ordi a un nombre de ", minimum, " a", maximum, ".\n\n\t Essaye de le deviner!\n\n")
            choix_du_joueur, choix_de_ordi = int(input()), randint(minimum, maximum)
    else:
        choix_du_joueur = int(input("\tRessayez\n\n"))


while True:
    valeur_incorrecte_verification()
    rejouer()
