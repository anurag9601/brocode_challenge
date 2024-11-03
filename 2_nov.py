#Problem 1
# Create a function that will build a staircase using the underscore _ and hash # symbols. A positive value denotes the staircase's upward direction and downwards for a negative value.

# Examples
# staircase(3) ➞ "__#\n_##\n###"
# __#
# _##
# ###

# staircase(7) ➞ "______#\n_____##\n____###\n___####\n__#####\n_######\n#######"
# ______#
# _____##
# ____###
# ___####
# __#####
# _######
# #######

# staircase(2) ➞ "_#\n##"
# _#
# ##

# staircase(-8) ➞ "########\n_#######\n__######\n___#####\n____####\n_____###\n______##\n_______#"
# ########
# _#######
# __######
# ___#####
# ____####
# _____###
# ______##
# _______#

def staircase(n):
    if(n > 0):
        for i in range(1,n+1):
            current_value = n - i
            for j in range(n):
                if(j<current_value):
                    print("_", end="")
                else:
                    print("#", end="")
            print()
    elif(n < 0):
        n = abs(n)
        for i in range(n):
            current_value = n - i
            for j in range(n, 0, -1):
                if(j>current_value):
                    print("_", end="")
                else:
                    print("#", end="")
            print()


