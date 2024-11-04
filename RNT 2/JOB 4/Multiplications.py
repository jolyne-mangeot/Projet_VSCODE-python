
N = int(input("Jusque quel nombre montrer la table de multiplication: "))
for i in range(1, N+1):
    print(f"Table de multiplication de {i} :")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print("")
