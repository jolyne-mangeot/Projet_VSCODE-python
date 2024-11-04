N = int(input(f"A partir de quel nombre N voulez vous multiplier 7 ? "))
nombre_resultats = int(input(f"Combien de résultats voulez vous ? "))
x = N*7

while nombre_resultats > 0:
    print(f"{N} x 7 = {x}")
    N+= 1
    x= N*7
    nombre_resultats -= 1

nombre_atteindre = int(input("Combien de fois voulez-vous multiplier 7 ? "))+1
for i in range (1, nombre_atteindre):
    print(f"{i} x 7 = {i*7}")
