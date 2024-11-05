board = [' ' for coordinates in range(9)]
Symbol = ['x','o','&','#','★','♥']

def Display_board():
    #imprimer un board de jeu où sont inscrites les coordonnées de jeu qui seront remplacées par les symboles joués
    print(f"| {board[0]} | {board[1]} | {board[2]} |" )
    print("-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |" )
    print("-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |" )

def Check_win(Symbole):
    #vérifier si le dernier placement de symbole permet de compléter une combinaison victorieuse pour le joueur
    pass

def TRY_int(input):
    #try si l'input est un entier ou non
    pass

Display_board()
board[2] = 4
Display_board()
print(board)
