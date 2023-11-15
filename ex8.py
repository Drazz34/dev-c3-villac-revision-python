resultats = {
    "Saturnin Ouinouin": 14,
    "Eglantine Lapine": 12,
    "Clotaire Camembert": 17,
    "Kévin Divin": 19,
    "Georgette Braguette": 8,
    "Antoinette Brouette": 18,
    "Kévin Choin": 19
}

for eleve, note in resultats.items():
    print("L'élève", eleve, "a obtenu la note de", note)

meilleur_eleve = max(resultats, key=resultats.get)
print("La meilleure note est obtenue par", meilleur_eleve, "avec un", resultats[meilleur_eleve], "/ 20.")
