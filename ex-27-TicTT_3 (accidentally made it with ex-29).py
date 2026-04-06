import numpy as np


def drawboard(board):
    print(f"\n  {board[0][0]} | {board[0][1]} | {board[0][2]}")
    print(" ---+---+---")
    print(f"  {board[1][0]} | {board[1][1]} | {board[1][2]}")
    print(" ---+---+---")
    print(f"  {board[2][0]} | {board[2][1]} | {board[2][2]}\n")


def line_match(game):
    for i in range(3):
        set_r = set(game[i])
        if len(set_r) == 1 and game[i][0] != " ":
            return game[i][0]
    return 0


def dia_match(game):
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != " ":
        return game[0][0]
    elif game[0][2] == game[1][1] == game[2][0] and game[0][2] != " ":
        return game[0][2]
    return 0


game = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]
players = [("Player 1", "X"), ("Player 2", "O")]
winner = None

for turn in range(9):
    curr_player_name, mark = players[turn % 2] 
    
    print(f"it's {curr_player_name} turn ({mark})")
    while True:
        r = int(input("input the row you want: ")) - 1
        c = int(input("input the column you want: ")) - 1
        if game[r][c] == " ":
            game[r][c] = mark
            break
        else:
            print("this space is taken, please try again.")    
    drawboard(game)
    if line_match(game) == line_match(np.transpose(game)) == dia_match(game) == 0:
        pass
    else:   break
        
if line_match(game) != 0:
    print(f"The winner is {curr_player_name}, they won horonzontally!")

if line_match(np.transpose(game)) != 0:
    print(f"The winner is {curr_player_name}, they won virtically!")

if dia_match(game) != 0:
    print(f"The winner is {curr_player_name}, they won diagonally!")
if dia_match(game) == line_match(game) == line_match(np.transpose(game)) == 0:
    print("it's a tie")