nombre = [8, 24, 48, 2, 16]

count = len([x for x in nombre if x % 3 == 0])
print(count)

prime = [i for i in range(0,100) if all(i%j!=0 for j in range(2,i)) and i>1]
print(prime)


nombresss = [30,20,10,50,60,40,50,40]
print(nombresss)
nombressstri = []
for i in nombresss:
    if not i in nombressstri:
        nombressstri += [i]

L = [10,10,30,40]
L = [x for i, x in enumerate(L) if x not in L[:i]]
print(L)