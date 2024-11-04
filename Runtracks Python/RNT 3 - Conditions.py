
variable_1 = "hihi"
variable_2 = "haha"
if variable_1 != variable_2:
    print(f"{variable_1} !! {variable_2} !! MUAHAHA")
else: print("...")

age = 19
if age < 18:
    print("no vote for yu")
else: print("woaw go vote")

for i in range(101):
    if i==26 or i==37 or i==88:
        print("")
    else: print(i)

for i in range(101):
    if i not in(26,37,88):
        print(i)

for i in range (1,101):
    if i%3==0 and i%5==0:
        print("cocacola")
    elif i%3==0:
        print("coca")
    elif i%5==0:
        print("cola")
    else: print(i)


for i in range (3,100):
    if all(i%j!=0 for j in range(2,i)):
        print(i)


#nombre_pair = int(input("Quel nombre à tester ? (pair/impair) "))
#if nombre_pair%2==0:
#    print("C'est pair !")
#else: print("C'est pas pair mv//")


alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in range(0, ((alphabet*5).index((alphabet*5)[-1])+1)*5):
    print((alphabet*5)[0:i])


#lettreindex = int(0)
#while lettreindex<alphabet5.index(alphabet5[-1])+1*5:
#    lettreindex+=1
#    print(alphabet5[0:lettreindex])
