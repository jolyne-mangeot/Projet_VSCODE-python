def TRY_coor(input):
    #try si l'input de coordonnée correspond à une case vide, au quel cas le tour se termine
    while True:
        try:
              coordinates = int(input(f"joueur {player}, choisis une position (1-9) : ")) -1
              if coordinates < 0 or coordinates >=9 or board[coordinates] != " ":
                print("choisis une position entre 1 et 9")
                continue
        except:
            print("Veuillez entrer un nombre entre 1 et 9")
            continue
