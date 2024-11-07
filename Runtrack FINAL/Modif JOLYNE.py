
board = [coordinates for coordinates in range(1,10)]
    #cette liste à répéter à chaque début de manche définit / réinitialise la
    # grille, générant 9 "coordinates" vierges

symbol = ['x','o','&','#','★','♥']
    #cette liste établit les différents symboles pouvant être utilisés pour
    # représenter le jeu de chaque joueur

players = [' ', ' ']
    #cette liste énumère et désigne le ou les deux joueurs participants aux
    # différentes manches

TURN = 0
    #cette variable compte le nombre de tours écoulés depuis le début de la
    # manche, permettant d'arrêter celle-ci lorsque les 9 tours sont écoulés

SYMBOL_J1 = ''
SYMBOL_J2 = ''
SCORE_J1 = ''
SCORE_J2 = ''


def Display_rules(y_n):
    #affiche ou non les règles du jeu, l'assignation des symboles et le
    # système de manches
    if y_n in ('o', 'oui', 'O', 'Oui', 'y', 'yes', 'Y', 'Yes'):
        print()
        Display_board()
        print()
        print("Voici les règles")
        print()
        return
    else :
        print()
        return


def Choose_symbol(player):
    #définit avec un input le choix de symbole réalisé par le joueur puis
    # supprime celui-ci de la liste disponible
    while True:
        print(symbol)
        for x in range(1, symbol.index(symbol[-1])+2):
            print("   ", end='')
            print(x, ",", sep='', end='')
        print()
        choice = input("Faites votre choix avec le numéro correspondant : ")
        try:
            choice = int(choice)
        except ValueError:
            print("Insérez un nombre entier désignant le symbole choisi : ")
            continue
        if 0 <= choice-1 <= symbol.index(symbol[-1]):
            players[player] = symbol.pop(choice-1)
            return
        else: 
            print("Insérez un nombre compris dans la sélection : ")
            continue


def Reset_board():
    board[0:9] = [' ' for coordinates in range(1,10)]

def Display_board():
    #imprimer un board de jeu où sont inscrites les coordonnées de jeu qui
    # seront remplacées par les symboles joués
    print(f"| {board[0]} | {board[1]} | {board[2]} |" )
    print("-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |" )
    print("-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |" )


def TRY_coor(input):
    #try si l'input de coordonnée correspond à une case vide, au quel cas le
    # tour se termine
    pass


def Check_win(Symbole):
    #vérifier si le dernier placement de symbole permet de compléter une
    # combinaison victorieuse pour le joueur
    if all(Symbole in board[x] for x in (0,3,6)) or all(Symbole in board[x]\
     for x in (1,4,7)) or all(Symbole in board[x] for x in (2,5,8)):
        return True
    
    elif all(Symbole in board[x] for x in (0,1,2)) or all(Symbole in board[x]\
     for x in (3,4,5)) or all(Symbole in board[x] for x in (6,7,8)):
        return True
    
    elif all(Symbole in board[x] for x in (2,4,6)) or all(Symbole in board[x]\
     for x in (0,4,8)):
        return True
    else:
        return False

def Launch_round():
    TURN +=1
    Reset_board()
    Display_board()
    TRY_coor(input("Quelle case souhaitez-vous jouer ? (1 à 9) "))
    pass



    #compile et initie l'intégralité des algorythmes composant le jeu,
    # permettant la délimitation de manches
Display_rules(input("Bienvenue au tic-tac-toe ! Voulez-vous visualiser les\
 règles avant de commencer ? (affichage de la grille coordonnée) o/n "))
print("Le premier joueur choisit le symbole qui le représentera pendant la\
 manche,")
print("Ce symbole doit être désigné à partir de la liste qui suit :")
Choose_symbol(0)
print("Le deuxième joueur choisit également son symbole conformément à la\
 liste")
Choose_symbol(1)
print("Le joueur 1 jouera donc avec le symbole :", players[0],\
 "et le joueur 2 :", players[1])
SYMBOL_J1 = players[0]
SYMBOL_J2 = players[1]
Launch_round()



    
