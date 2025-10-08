liste_nombres = [8, 4, 6, 1, 5]
plus_petit = liste_nombres[0]

for nombre in liste_nombres:
    if nombre < plus_petit:
        plus_petit = nombre

print(f"La liste est : {liste_nombres}")
print(f"Le plus petit élément est : {plus_petit}")