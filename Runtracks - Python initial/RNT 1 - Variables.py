#job4 et 5, afficher une variable et la variable à l'envers
import string
alphabet = string.ascii_lowercase
alphabetreverse = string.ascii_lowercase[::-1]

### variable[x] désigne directement la valeur à l'emplacement de l'index x (de 0 à max -1 qui désigne la dernière valeur).
#   Il est possible d'afficher plusieurs de ces index en utilisant une organisation particulière [x:y:z], respectivement [départ:fin:en commençant par]
#   [::-1] commence donc le "slice", le dénombrage, en commençant par la dernière valeur
print(alphabet)
print(alphabetreverse)


#job5 et 6, créer des variables qui peuvent être :
#   des string, str("chaîne de caractères")
#   des nombres entiers qui peuvent être arrondis avec round ou non, int(12.3)
#   des nombres flottants, décimaux, float(12,3)
#   une variable boléenne qui représente un état binaire, oui/non, True/False, 0/1
ma_string = 'ceci est ma string'
print(ma_string)

#   ces variables peuvent être manipulées par des opérations, "inputted" par l'utilisateur, modifiées par ces différents facteurs, etc.
x = int(3.1)
y = int(14)
z = x*y
print(z)

#job10, extrait de ce qui peut être intégré à un plus complexe système d'inventaire en utilisant des variables dont les données sont évolutives
#   un formattage adapté aux données traitées, etc.
gourde_prix = 4.99
gourde_stock = int(15 - int(input("Indiquez la quantité désirée:")))

#   le formattage du print() peut être fait avec le paramètre f"", qui permet de n'utiliser qu'une paire de ""
print(f"Il reste donc {gourde_stock} gourdes.")
print("Il reste", gourde_stock, "gourdes.")