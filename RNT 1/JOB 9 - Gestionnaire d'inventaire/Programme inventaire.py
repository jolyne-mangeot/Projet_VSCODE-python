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
