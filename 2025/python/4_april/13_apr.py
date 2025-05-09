#Mutate string problem

def mutate_string(string, position, character):
    # another way
    # string_l = list(string)
    # string_l[position] = character
    # return "".join(string_l)
    return string[:position] + character + string[position + 1:]
    
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    # print(s_new)

# Kevin and Stuart want to play the 'The Minion Game'.

# Game Rules
# Both players are given the same string, .
# Both players have to make substrings using the letters of the string .
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

# Scoring
# A player gets +1 point for each occurrence of the substring in the string .

# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

def minion_game(string):
    # your code goes here
    stuart_score = 0
    kevin_score = 0
    
    n = len(string)
    
    for i in range(n):
        if string[i] in "AEIOU":
            kevin_score += n - i
        else:
            stuart_score += n - i
    
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif stuart_score < kevin_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")  

if __name__ == '__main__':
    s = input()
    # minion_game(s)