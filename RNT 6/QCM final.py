print(len("bonjour"))

a = 5
b = "10"
resultat = a / 1
print(resultat)

i,j = 3, 4
print(i, j)

A1 = 4
A2 = 7
A3 = 1
A4 = 9
for i in [1, 98, 36, 5, 6, 33, 42, 77, 48, 70, 31]:
    A1=A2
    A2=A3
    A3=A4
    A4=i

print(A1)
n=0
for i in range (0,11):
    n+=1

print(n)

def f(n):
    if n%2==0:
        return True
    else:
        return False

print(f(2))

def fon(n):
    p = 1
    for k in range(1,n+1):
        p=p*k
    return p

print(fon(3))

A21=[1,2,3]
A22=['3']
A23=7*A21
print(A23)
