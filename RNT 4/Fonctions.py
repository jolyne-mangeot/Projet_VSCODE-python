
#job 1
def hihi():
    print("MUAHAHA")
#hihi()

#job 2
def haha(fname):
    print(f"{fname} MUAHAHA")
haha("déniodhéio")

#job 3
def somme(fint, pint):
    print(f"{fint} + {pint} = {fint + pint}")
#somme(int(input("nb 1 stp ")), int(input("input your 2 nombre stp thx ")))

#job 4
def get_hello(nombre):
     return nombre**2

#job 5
def calcul(nb1, opér, nb2, résultat):
            if opér == "+":
                résultat = nb1 + nb2
            elif opér == "-":
                résultat = nb1 - nb2
            elif opér == "*":
                résultat = nb1 * nb2
            elif opér == "/":
                résultat = nb1 / nb2
            elif opér == "**":
                résultat = nb1 ** nb2
            elif opér == "//":
                résultat = nb1 // nb2
            else: opér = input("L'opérateur doit être l'un de ces caractères : +, -, /, *, ** (puissance), // (division au résultat entier) : ")
            print(nb1, opér, nb2, "=", résultat)

#calcul(int(input("NB1 ")), str(input("opération ")), int(input("NB2 ")), int())

#job 6
def posinega(nombre):
     if nombre >= 0:
          print("posi")
     else: print("négat")

posinega(25)
posinega(-23)
posinega(0)

#job 7
def langage(langue):
     if langue == "java":
          print("javafezfzfze")
     elif langue == "python":
          print("serppeeeennnnt")

#job 8
def info(fruileg, saison):
     if fruileg == "fruit" and saison == "été":
          print("poire fraise ttt")
     elif fruileg == "légume" and saison == "été":
          print("artichauththtuthuthtu")
     elif fruileg == "fruit" and saison == "hiver":
          print("orange")
     elif fruileg == "légume" and saison == "hiver":
          print("carotte")
     else: return

#job 9
def moyenne(a,b,c):
     return (float(a+b+c))/3


#job 10
def pair(nombre):
     if int(nombre) >= int(1):
          if int(nombre)%2==0:
               return "pair"
          else: return "impair"
     else: pass

#print(pair(input("hihiahahahahaha nombre stp ")))

#job 11
def heure(minutes):
     print(minutes//60, "heure", minutes%60, "minutes")

heure(int(input("insère des minutes ")))
