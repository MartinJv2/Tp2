"""
Ce code a ete ecrit pas Jeremy Martin. Groupe : 403
le code fait en sorte que l`ordinateur joue un jeu de devinette avec le joueur
"""

from random import randint

minimum, maximum, essais = input("Entrez la borne maximale"), input("Entrez la borne minimale"), 0
if minimum == '':
	minimum = 100
else:
	minimum = int(minimum)
if maximum == '':
	maximum = 100
else:
	maximum = int(maximum)
choix_du_joueur, choix_de_ordi = int(input(f"Devinez un nombre de  {minimum}  a {maximum} .\n\n")), randint(minimum,
																											maximum)
jouer = True


def valeur_incorrecte_verification():
	"""
	verifie si la reponse donne par le joueur est correct.
	"""
	if choix_du_joueur > choix_de_ordi:
		print("\tTa reponse est plus grande que celle de l`ordi\n\n")
	elif choix_du_joueur < choix_de_ordi:
		print("\tTa reponse est plus petite que celle de l`ordi\n\n")


def rejouer():
	"""
	verifie si le joueur peut rejouer. Si oui, ca le demande de rejouer.
	"""
	global choix_de_ordi, essais, choix_du_joueur, jouer

	essais += 1

	if choix_du_joueur == choix_de_ordi:
		demande_de_rejouer = input(
			f"\tTa eu la reponse correct!!! ( {essais} essais)\n\n Recommencer? (non=1 oui=autre)\n\n")

		if demande_de_rejouer == "1":
			jouer = False
		else:
			minimal, maximal, essais = input("Entrez la borne maximale"), input("Entrez la borne minimale"), 0

			if minimal == '':
				minimal = 100
			else:
				minimal = int(minimal)
			if maximal == '':
				maximal = 100
			else:
				maximal = int(maximal)
				print(f"L`ordi a un nombre de {minimal}  a {maximal} .\n\n\t Essaye de le deviner!\n\n")
				choix_du_joueur, choix_de_ordi = int(input()), randint(minimal, maximal)

	else:
		choix_du_joueur = int(input("\tRessayez\n\n"))


while jouer:
	valeur_incorrecte_verification()
	rejouer()
