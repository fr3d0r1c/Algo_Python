semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]
for jour in semaine:
    if jour == "lundi" or jour == "mardi" or jour == "mercredi" or jour == "jeudi":
        print(f"{jour} - Au travail")
    elif jour == "vendredi":
        print(f"Chouette c\'est {jour}")
    else:
        print(f"{jour} - Repos ce week-end")