# Exercice 5 : Parcourir une matrice carrée 2x2

# On crée une matrice 2x2 (liste de listes)
matrice = [
    [1, 2],
    [3, 4]
]

# Parcours de la matrice avec des boucles for imbriquées
for i in range(len(matrice)):          # i = index de ligne
    for j in range(len(matrice[i])):   # j = index de colonne
        print(f"Ligne {i}, Colonne {j} -> Élément = {matrice[i][j]}")
