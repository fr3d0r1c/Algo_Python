from statistics import mean

notes_etudiant = [14, 9, 13, 15, 12]
moyenne = mean(notes_etudiant)
note_min = min(notes_etudiant)
note_max = max(notes_etudiant)

for note in notes_etudiant:
    if note >= 10 and  note < 12:
        print(f"{note:.2f} - Mention Passable")
    elif note >= 12 and note < 14:
        print(f"{note:.2f} - Mention Assez bien")
    elif note >= 14:
        print(f"{note:.2f} - Mention Bien")
    else:
        print(f"{note:.2f} - Pas de diplome")

print(f"Moyenne : {moyenne:.2f}")
print(f"Note minimal : {note_min:.2f}")
print(f"Note Maximal : {note_max:.2f}")