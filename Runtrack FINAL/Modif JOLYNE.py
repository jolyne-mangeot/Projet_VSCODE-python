    #cette liste définit / réinitialise la grille, générant 9 "coordinates" vierges
board = [' ' for coordinates in range(9)]
Symbol = ['x','o','&','#','★','♥']

    #ces variables qui se définissent à partir de la liste Symbol assignent à chaque joueur le caractère joué lors des manches
Symbol_J1 = ' '
Symbol_J2 = ' '

    #cette variable compte le nombre de tours écoulés depuis le début de la manche, permettant d'arrêter celle-ci lorsque les 9 tours sont écoulés
Turn = 0

def Display_rules():
    #affiche ou non les règles du jeu, l'assignation des symboles et le système de manches
    pass

def Display_board():
    #imprimer un board de jeu où sont inscrites les coordonnées de jeu qui seront remplacées par les symboles joués
    print(f"| {board[0]} | {board[1]} | {board[2]} |" )
    print("-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |" )
    print("-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |" )

def Check_win(Symbole):
    #vérifier si le dernier placement de symbole permet de compléter une combinaison victorieuse pour le joueur
    #   va retourner : False ou True afin de l'utiliser comme condition
    if Symbole in board[0]:

def TRY_int(minimum, maximum):
    #try si l'input est un entier ou non afin de renvoyer un input correct compris entre les deux valeurs assignées (utilisation pour le choix du symbole et du jeu)
    pass

def TRY_coor(input):
    #try si l'input de coordonnée correspond à une case vide, au quel cas le tour se termine
    pass

def Launch_game():
    #compile et initie l'intégralité des algorythmes composant le jeu, permettant la délimitation de manches
    pass

