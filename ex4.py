nombres = [34, 5, 7, 11, 16, 55, 6, 23, 100, 88]

def maximum(liste):
    maxi = liste[0]
    for i in liste:
        if i >= maxi:
            maxi = i
    return maxi

def minimum(liste):
    mini = liste[0]
    for i in liste:
        if i <= mini:
            mini = i
    return mini


def moyenne(liste):
    total = 0
    for i in liste:
        total += i
    calcul_moyenne = total / len(liste)
    return calcul_moyenne


print(maximum(nombres))
print(minimum(nombres))
print(moyenne(nombres))
