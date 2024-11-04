import string
alphabet = string.ascii_lowercase
alphabetreverse = string.ascii_lowercase[::-1]
print(alphabet)
print(alphabetreverse)

ma_string = 'ceci est ma string'
print(ma_string)

x = int(3.1)
y = int(14)
z = int(1)
print(x * y)

gourde_prix = 4.99
gourde_stock = int(15 - int(input("Indiquez la quantité désirée:")))


print(f"Il reste donc {gourde_stock} gourdes.")

print("Il reste", gourde_stock, "gourdes.")
