# Tic Tac Toe (it can handle any number of grid board)

def tic_tac_toe(board):
    rows_l = []
    cols_l = []
    hors_l = [[],[]]
    l = 0
    r = len(board) - 1

    for i in range(len(board)):
        rows_l.append(board[i])
        for j in range(len(board)):
            if len(cols_l) <= j:
                cols_l.append([board[i][j]])
            else:
                cols_l[j] = cols_l[j] + [board[i][j]]

        hors_l[0].append(board[i][l])
        hors_l[1].append(board[i][r])
        l += 1
        r -= 1

    final_l = rows_l + cols_l + hors_l
    for pattern in final_l:
        set_p = set(pattern)
        if len(set_p) == 1:
            return list(set_p)[0]
    return "Draw"

print(tic_tac_toe([
  ["X", "O", "X"],
  ["O", "X",  "O"],
  ["O", "X",  "X"]
]))