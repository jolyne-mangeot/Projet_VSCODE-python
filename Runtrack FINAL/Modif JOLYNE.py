

    #cette liste définit / réinitialise la grille, générant 9 "coordinates" vierges
board = [' ' for coordinates in range(9)]
symbol = ['x','o','&','#','★','♥']
players = [' ', ' ']
    #cette variable compte le nombre de tours écoulés depuis le début de la manche, permettant d'arrêter celle-ci lorsque les 9 tours sont écoulés
turn = 0


def Display_rules():
    #affiche ou non les règles du jeu, l'assignation des symboles et le système de manches
    pass


def Choose_symbol(player):
    while True:
        choix = input(symbol )
        try:
            choix = int(choix)
        except ValueError:
            print("Insérez un nombre entier désignant le symbole choisi")
            continue
        if 0 <= choix <= symbol.index(symbol[-1]):
            players[player] = symbol.pop(choix)
            return
        else: 
            print("Insérez un nombre compris dans la sélection")
            continue


def Display_board():
    #imprimer un board de jeu où sont inscrites les coordonnées de jeu qui seront remplacées par les symboles joués
    print(f"| {board[0]} | {board[1]} | {board[2]} |" )
    print("-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |" )
    print("-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |" )


def TRY_coor(input):
    #try si l'input de coordonnée correspond à une case vide, au quel cas le tour se termine
    pass


def Check_win(Symbole):
    #vérifier si le dernier placement de symbole permet de compléter une combinaison victorieuse pour le joueur
    #   va retourner : False ou True afin de l'utiliser comme condition
    if all(Symbole in board[x] for x in (0,3,6)) or all(Symbole in board[x] for x in (1,4,7)) or all(Symbole in board[x] for x in (2,5,8)):
        return True
    elif all(Symbole in board[x] for x in (0,1,2)) or all(Symbole in board[x] for x in (3,4,5)) or all(Symbole in board[x] for x in (6,7,8)):
        return True
    elif all(Symbole in board[x] for x in (2,4,6)) or all(Symbole in board[x] for x in (0,4,8)):
        return True
    else:
        return False

  
    

def Launch_game():
    #compile et initie l'intégralité des algorythmes composant le jeu, permettant la délimitation de manches
    print("le premier joueur choisit le symbole qui le représentera pendant la manche")
    print("Ce symbole doit être désigné à partir d'une liste qui suit :")
    Choose_symbol(0)

    print(players)

    print("Le deuxième joueur choisit également son symbole conformément à la liste")
    Choose_symbol(1)
    print("Le joueur 1 jouera donc avec le symbole : " + players[0] + " et le joueur 2 : " + players[1])


    

Launch_game()