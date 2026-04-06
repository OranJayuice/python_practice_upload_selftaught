import numpy as np
game = [[1, 1, 1],
	    [2, 1, 0],
	    [2, 2, 2]]
set_r = ()
set_c = ()
def line_match(game):
    for i in range (3):
        set_r = set(game[i])
        if len(set_r) == 1 and game [i][0] !=0 :
            return game[i][0]
    return 0
def dia_match(game):
    if game[0][0] == game[1][1] == game[2][2] and game[0][0] != 0:
        return game[0][0]
    elif game[0][2] == game[1][1] == game[2][0] and game[0][2] !=0:
        return game[0][2]
    return 0
if line_match(game) > 0:			
	print (str(line_match(game)) + str(" row wins!"))
if line_match(np.transpose(game)) > 0:
	print (str(line_match(np.transpose(game))) + str(" column wins!")) #trans the array sideway lol
if dia_match(game) > 0:
	print (str(dia_match(game)) + str(" diagonal wins!"))