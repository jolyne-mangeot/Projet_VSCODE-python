for x in range(20):
    print(x+1)

y = 0
while y in range(20):
    print(y)
    y += 2

for z in range(20):
    print(z*z)

table = int(input("Montrer la table de multiplication de : "))
for w in range(15):
    print(table*(w+1))

N = int(input("Jusque quel nombre montrer la table de multiplication: "))
for i in range(1, N+1):
    print(f"Table de multiplication de {i} :")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("")

nombre_atteindre = int(input("Combien de fois voulez-vous multiplier 7 ? "))+1
for i in range (1, nombre_atteindre):
    print(f"{i} x 7 = {i*7}")

for i in range(1,13):
    print(f"Tour {i}: {i*3-2}")

m=int(0)
for i in range(1,13):
    m+=2
    print(f"Tour {i}: {m}")

print("P - I")
for i in range(15):
    print(f"{i*2} - {i*2+1}")
