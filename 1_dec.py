#Problem 1

# Bobby is troubleshooting a challenge he is attempting on Edabit. He needs to devise a function whose argument is the size of a square array. The function must return the array with the diagonals set to 1 and all the other members set to 0. His code is in the Code tab. Two of the lines contain bugs. Can you help him?

# Examples
# help_bobby(1) ➞ [[1]]

# help_bobby(3) ➞ [
#   [1, 0, 1],
#   [0, 1, 0],
#   [1, 0, 1]
# ]

# help_bobby(4) ➞ [
#   [1, 0, 0, 1],
#   [0, 1, 1, 0],
#   [0, 1, 1, 0],
#   [1, 0, 0, 1]
# ]

#Solution
def help_bobby(n):
    final = []
    count = 1
    for i in range(n):
        temp = []
        for j in range(n):
            if(i==j):
                temp.append(1)
            elif(n-count == j):
                temp.append(1)
            else:
                temp.append(0)
        final.append(temp)
        count += 1
    return final

#Problem 2

# Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.

# Examples
# tic_tac_toe([
#   ["X", "O", "X"],
#   ["O", "X",  "O"],
#   ["O", "X",  "X"]
# ]) ➞ "X"

# tic_tac_toe([
#   ["O", "O", "O"],
#   ["O", "X", "X"],
#   ["E", "X", "X"]
# ]) ➞ "O"

# tic_tac_toe([
#   ["X", "X", "O"],
#   ["O", "O", "X"],
#   ["X", "X", "O"]
# ]) ➞ "Draw"

#Solution
def tic_tac_toe(state):
    for i in range(len(state)):
        if(state[i][0] == state[i][1] == state[i][2]):
            return state[i][0]
    for i in range(len(state)):
        if(state[0][i] == state[1][i] == state[2][i]):
            return state[j][i]
    if(state[0][0] == state[1][1] == state[2][2]):
        return state[0][0]
    elif(state[0][2] == state[1][1] == state[2][0]):
        return state[0][2]
    else:
        return "Draw"
        