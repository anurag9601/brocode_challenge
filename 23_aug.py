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

#Problem 3
# This problem is a continuation of Uno Part 1 (although you don't need to complete that problem to complete this one).
# It's your turn to play again. Create a function that takes as its arguments (1) your hand (a list of cards), and (2) the face-up card. In Uno, you are able to play a card from your hand if either:
# One of the card colors in your hand matches the face-up card's color.
# One of the card numbers in your hand matches the face-up card's number.
# Write a function that will return:
# "Uno!" if after playing your card, you are left with a single card.
# "You won!" if after playing your card, you are left with zero cards (an empty list).
# "Keep going..." otherwise.
#Examples: 
# decision(["yellow 3", "red 3"], "red 10") ➞ "Uno!"
# decision(["blue 1"], "blue 5") ➞ "You won!"
# decision(["blue 1", "green 2", "yellow 4", "red 2"], "blue 5") ➞ "Keep going..."

#Solution 3
def decision(lst_of_cards, remain_card):
    split_remain_card = remain_card.split(" ")
    for i in lst_of_cards:
        split_card = i.split(" ")
        if(split_card[0] == split_remain_card[0] or split_card[1] == split_remain_card[1]):
            if(len(lst_of_cards) == 1):
                return "You won!"
            elif(len(lst_of_cards) == 2):
                return "Uno!"
            else:
                return "Keep going..."
    return "Keep going..."



