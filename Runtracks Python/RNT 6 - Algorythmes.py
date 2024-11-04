def rectangle(largeur, hauteur):
    if largeur >0 and hauteur >0:
        print("|" + "-"*(largeur-2) + "|")
    
    for x in range(hauteur-2):
        print("|" + " "*(largeur-2) + "|")
    
    if hauteur >1:
        print("|" + "-"*(largeur-2) + "|")


def triangle(hauteur):
    if hauteur >0:
        print(" "*(hauteur-1) + "/" + "\ ")
    
    x = hauteur-2
    y = 2
    while x >0:
        print(f"{" "*(x)}/{" "*(y)}\ ")
        x-=1
        y+=2
    
    if hauteur >1:
        print(f"/{"_"*((hauteur-1)*2)}\ ")


def diagonale(ratio):
    ratio +=1
    if ratio >0:
        print(f"+{"-"*(ratio+1)}+")
    x = ratio
    y = 1
    z = 0
    while x >=0:
        print(f"|{"#"*x}{" "*y}{"#"*z}|")
        x -=1
        z +=1
    if ratio >0:
        print(f"+{"-"*(ratio+1)}+")


for i in range(0,6):
    rectangle(i,i)
    print("")

for i in range(0,6):
    triangle(i)
    print("")

for i in range(0,6):
    diagonale(i)
    print("")

#/\
#
# /\
#/__\

#code césar mais pas fini
def code_césar(décal, message):
    alphabet = "abcdefghijklmnopqrstuvwyxz"
    index =0
    for lettres in alphabet:
        if lettres in message:
            message[message.find(lettres)] = alphabet[index+décal]
        index+1

code_césar(int(1),"je suis une tomate")
