text = open("texte_ex7.txt", "r")
lignes = text.read()
print(lignes)

nombre_mots = len(lignes.split())
print(nombre_mots)
text.close()

new_text = open("nombre_mots.txt", "w")
new_text.write(str(nombre_mots))
new_text.close()
