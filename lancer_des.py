"""
Énoncé : Le but de cet exercice est de générer 6 lancer de dés aléatoires, allant de 1 à 6.
Votre script doit récupérer ces lancers de dés dans la variable lancers.
"""

import random

lancers = []
for _ in range(6):
    nombre = random.choice(range(1, 7))
    lancers.append(nombre)
    print(nombre)