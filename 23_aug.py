#Problem 1
# There are two players, Alice and Bob, each with a 3-by-3 grid. A referee tells Alice to fill out one particular row in the grid (say the second row) by putting either a 1 or a 0 in each box, such that the sum of the numbers in that row is odd. The referee tells Bob to fill out one column in the grid (say the first column) by putting either a 1 or a 0 in each box, such that the sum of the numbers in that column is even.
# Alice and Bob win the game if Alice’s numbers give an odd sum, Bob’s give an even sum, and (most important) they’ve each written down the same number in the one square where their row and column intersect.
#Examples:
# magic_square_game([2, "100"], [1, "101"]) ➞ False
# magic_square_game([2, "001"], [1, "101"]) ➞ True
# magic_square_game([3, "111"], [2, "011"]) ➞ True
# magic_square_game([1, "010"], [3, "101"]) ➞ False

#Solution 1
def magic_square_game(alice,bob):
    grid = [
        ["X","X","X"],
        ["X","X","X"],
        ["X","X","X"]
        ]
    try:
        row_input = [*alice[1]]
        column_input = [*bob[1]]
        for i in range(len(grid)):
            if(alice[0] == i+1):
                for j in range(len(grid[i])):
                    if(grid[i][j] != "X" and grid[i][j] != row_input[j]):
                        return False
                    else:
                        grid[i][j] = row_input[j]
            for j in range(len(grid[i])):
                if(j+1 == bob[0]):
                    if(grid[i][j] != "X" and grid[i][j] != column_input[i]):
                        return False
                    else:
                        grid[i][j] = column_input[i]
        return True
    except:
        print("Invalid input")


#Problem 2
# Create a function that, given a phrase and a number of letters guessed, returns a string with hyphens - for every letter of the phrase not guessed, and each letter guessed in place.
#Examples:
# hangman("helicopter", ["o", "e", "s"]) ➞ "-e---o--e-"
# hangman("tree", ["r", "t", "e"]) ➞ "tree"
# hangman("Python rules", ["a", "n", "p", "r", "z"]) ➞ "P----n r----"
# hangman("He"s a very naughty boy!", ["e", "a", "y"]) ➞ "-e"- a -e-y -a----y --y!"

#Solution 2
def hangman(word, guessLetters):
    result = ""
    spacial_character_list = [" ", '"', "!", "'", ",", "?"]
    for i in word:
        if (i in spacial_character_list):
            result += i
        elif(i in guessLetters):
            result += i
        else:
            result += "-"
    return result


