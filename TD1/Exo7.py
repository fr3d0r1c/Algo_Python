import random

# Exercice 7 : La puce saute de 0 à 5

# Position de départ et d’arrivée
depart = 0
arrivee = 5

# Position actuelle
position = depart

# Compteur de sauts
sauts = 0

# Boucle jusqu’à ce que la puce atteigne la position d’arrivée
while position != arrivee:
    # Choisir un saut aléatoire : -1 (arrière) ou +1 (avant)
    saut = random.choice([-1, 1])
    position += saut
    sauts += 1
    print(f"Saut {sauts}: la puce est maintenant en position {position}")

# Résultat final
print(f"\nLa puce a atteint la position {arrivee} après {sauts} sauts.")
