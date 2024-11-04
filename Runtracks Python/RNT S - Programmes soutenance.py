#
# Simuler l'ajout d'un produit à un inventaire en ligne
#
produit_1 = []
produit_1.append(input("Indiquez le nom du premier produit : ")) 
produit_1.append(float(input(f"Indiquez le prix de {produit_1[0]} : ")))
produit_1.append(int(input(f"Indiquez le nombre de {produit_1[0]} qu'il y a en stock : ")))

print(f"- {produit_1[0]} -    {produit_1[1]}€ - {produit_1[2]} en stock")

print(f"Il y a {produit_1[2]} {produit_1[0]} en stock.")
produit_1_achetes = int(input("Combien en voulez-vous ? "))
coût_final = round(float(produit_1_achetes) * float(produit_1[1]) * float(1.1), 2)
print(f"Le prix original est de {produit_1[1]}, en prenant en compte le nombre choisi et les taxes, cela vous coûtera donc {coût_final}€.")
produit_1[2] -= produit_1_achetes
print(f"Il reste {produit_1[2]} {produit_1[0]}")

#
# Enumérer les particularités d'un triangle à partir des longueurs de ses côtés
# 
a = float(input("Longueur a : "))
b = float(input("Longueur b : "))
c = float(input("Longueur c : "))
hypo = max(a,b,c)
def puissance(nombre):
    return nombre**2

if hypo <= a+b+c-hypo:
    print("OK C UN TRIANGLE")
    if a==b==c:
        print("C EQUILATEREALL")
    elif round(puissance(hypo), 0) == round(puissance(a) + puissance(b) + puissance(c),0) - round(puissance(hypo),0) and (a==b or b==c or c==a):
        print("jakpot")
    elif round(puissance(hypo),0) == puissance(a) + puissance(b) + puissance(c) - puissance(hypo):
        print("C RECTANGLE BRAVOOOOO")
    elif a==b or b==c or c==a:
        print("Triangle isocèle")
    else: print("Triangle lambda")
else: print("C'est pas un triangle tho")

