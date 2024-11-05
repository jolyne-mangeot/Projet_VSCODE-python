# Afficher la grille "board"
board = [' ' for _ in range(9)]

def display_board():
    print(" "*13)
    print(f"| {board[0]} | {board[1]} | {board[2]} |" )
    print("-"*13)
    print(f"| {board[3]} | {board[4]} | {board[5]} |" )
    print("-"*13)
    print(f"| {board[6]} | {board[7]} | {board[8]} |" )
    print(" "*13)
print("")
#Vérifie si il y'a un gagnant 
def check_winner(player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8], #Lignes
        [0,3,6],[1,4,7],[2,5,8], #Colonnes
        [0,4,8],[2,4,6] #Diagonales
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

#Vérifier si la grille est pleine
def grille_pleine():
    return ' ' not in board

#Boucle de jeu
def play_game():
    current_player = "X" #Commence par le joueur X
    while True:
        display_board()

        #demande au joueur de saisir sa position
        try:
            position = int(input(f"joueur {current_player}, choisis une position (1-9) : ")) -1
            if position < 0 or position >=9 or board[position] != " ":
                print("position invalide. retry")
                continue
        except ValueError:
            print("Veuillez entrer un nombre entre 1 et 9")
            continue

        #MAJ de la grille avec e symbole du joueur
        board[position] = current_player

        #Vérifie si le joueur actuel a gagné
        if check_winner(current_player):
            display_board()
            print(f"Félicitations !!!! le joueur {current_player} à gagné !!")
            break

        #vérifie si il y a match nul
        if grille_pleine():
            display_board()
            print("Match Nul :/ ")
            break

        #Changer de joueur
        current_player = 'O' if current_player == "X" else "X"

        #Lancement du jeu
play_game()