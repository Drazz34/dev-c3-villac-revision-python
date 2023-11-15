def phrase():
    saisie_utilisateur = input("Saisissez une phrase : ")
    saisie_maj = saisie_utilisateur.upper()
    saisie_min = saisie_utilisateur.lower()
    nombre_mots = len(saisie_utilisateur.split())

    print(saisie_maj)
    print(saisie_min)
    print(f"Nombre de mots: {nombre_mots}")


phrase()
