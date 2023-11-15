resultats = {
    "Saturnin Ouinouin": 14,
    "Eglantine Lapine": 12,
    "Clotaire Camembert": 17,
    "Kévin Divin": 19,
    "Georgette Braguette": 8,
    "Antoinette Brouette": 18,
    "Kévin Choin": 19
}

# Trouver la note la plus élevée
meilleure_note = max(resultats.values())

# Filtrer pour obtenir les élèves ayant la meilleure note
meilleurs_eleves = [eleve for eleve, note in resultats.items() if note == meilleure_note]

# Trier ces élèves par ordre alphabétique
meilleurs_eleves_tries = sorted(meilleurs_eleves)

# Sélectionner le premier élève de la liste triée
meilleur_eleve = meilleurs_eleves_tries[0]

# Afficher le résultat
print(meilleur_eleve, resultats[meilleur_eleve])
