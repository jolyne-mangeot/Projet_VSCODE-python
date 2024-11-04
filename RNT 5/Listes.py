#job1, créer une liste
fruits = ['pomme', 'cerise', 'orange']
print(fruits)

#job2, afficher l'élément d'une liste à un certain index
print(fruits[1])

#job3, ajouter un élément à la fin d'une liste
fruits.append('melon')
print(fruits)

#job4, ajouter un élément à un index précis dans une liste
fruits.insert(2, 'mangue')
print(fruits)

#job5 et 6, manipuler les éléments d'une liste
def liste1():
    liste = [1, 2, 3, 4, 5]
    print(liste)
    print(liste[1])
    liste[3] = liste[2] + liste[4]
    print(liste)
    print(liste[-1])
    liste[0], liste[-1] = liste[-1], liste[0]
    print(liste)
print(liste1())

#job7, générer un compte de combien de valeurs sont des multiples de 3
nombre = [8, 24, 48, 2, 16]
count = len([x for x in nombre if x %3==0])
print(count)

#job8, ajouter plusieurs valeurs à une ilste existante
nombresnouveaux = (9,7,84,91)
nombre.extend(nombresnouveaux)
print(sum(x for x in nombre if x%2==0))

#job9, ranger les valeurs en ordre croissant avec la fonction list.sort()
nombres = [8,24,27,48,2,16,9,102,7,84,91]
#nombres.sort()
print(nombres[0], nombres[-1])

#afficher la valeur maximum et minimum parmi une sélection
print(max(nombres))
print(min(nombres))

#job10, faire le produit de tous les nombres compris entre deux valeurs à partir d'une liste
import math
print([x for x in nombres if x >=25 and x <=90])
print(math.prod(x for x in nombres if x >=25 and x <=90))

#job11, ajouter +1 à tous les éléments d'une liste
nombress = [7,11,42,39,2]
print(nombress)
nombress = [x+1 for x in nombress]
print(nombress)

#job12, organiser une liste en ordre croissant sans utiliser sort()
print(nombres)
for i in range(len(nombres)):
    for j in range(i+1, len(nombres)):
        if nombres[i] > nombres[j]:
            nombres[i], nombres[j] = nombres[j], nombres[i]
print(nombres)

#job13, modifier la liste afin d'en supprimer les doublons sans utiliser de fonction intégrée
L = [10,10,30,40]
L = [x for i, x in enumerate(L) if x not in L[:i]]
print(L)

#job14, afficher tous les mots dont le nombre de lettre dépasse n défini par l'utilisateur
def my_long_word(n, s):
    return [word for word in s.split() if word.index(word[-1])+1 > n]

print(my_long_word(3, "La peur est le chemin vers le côté obscur, la peur mène à la colère, la colère mène à la haine, la haine mène à la souffrance"))

#job15, arrondir des nombres décimaux et les ordonner en ordre croissant sans utiliser directement round() et sort()
N = [22.4, 4.0, 16.22,9.10, 11.00, 12.22, 14.20, 5.20, 17.60]
for i in range(len(N)): 
    N[i] = int(N[i] + 0.5)

for i in range(len(L)):
    for j in range(i+1, len(L)): 
        if N[i] > N[j]: N[i], N[j] = N[j], N[i]
