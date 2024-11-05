#job1 à 3, afficher des ranges de nombres grâce aux boucles for et while
for x in range(20):
    print(x+1)

#   for est utilisable dans un contexte local, boucle dont on connaît le point de départ et d'arrivée
#   à l'inverse, while permet d'aggrémenter des variables globales et de les utiliser en arguments afin de répéter le bon nombre de fois une loop
y = 0
while y in range(20):
    print(y)
    y += 2

for z in range(20):
    print(z*z)

#job4 et 7, introduire un input, un formattage et des boucles doubles afin de réaliser des actions dans d'autres
#   ici les multiplications sont des sous-actions à la boucle permettant d'augmenter le facteur principale du produit à chaque fin de table
N = int(input("Jusque quel nombre montrer la table de multiplication: "))
for i in range(1, N+1):
    print(f"Table de multiplication de {i} :")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("")

nombre_atteindre = int(input("Combien de fois voulez-vous multiplier 7 ? "))+1
for i in range (1, nombre_atteindre):
    print(f"{i} x 7 = {i*7}")

#job7 et 8, répéter des tours et montrer les possibilités d'afficher, calculer et initier des actions qui dépendent de la variable locale
for i in range(1,13):
    print(f"Tour {i}: {i*3-2}")

m=int(0)
for i in range(1,13):
    m+=2
    print(f"Tour {i}: {m}")

#job9, formatter un affichage en tableau
print("P - I")
for i in range(15):
    print(f"{i*2} - {i*2+1}")
