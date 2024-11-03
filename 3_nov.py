#Problem 1
# Write a function that groups a string into parentheses clusters. Each cluster should be balanced.
# Examples
# split("()()()") ➞ ["()", "()", "()"]

# split("((()))") ➞ ["((()))"]

# split("((()))(())()()(()())") ➞ ["((()))", "(())", "()", "()", "(()())"]

# split("((())())(()(()()))") ➞ ["((())())", "(()(()()))"]

# Notes
# All input strings will only contain parentheses.
# Balanced: Every opening parens ( must exist with its matching closing parens ) in the same cluster.

#Solution 1
def split(s):
    result = []
    temp = ""
    left_paren_count = 0
    right_paren_count = 0
    for i in s:
        if(left_paren_count > 0 and right_paren_count > 0 and left_paren_count == right_paren_count):
            result.append(temp)
            left_paren_count = 0
            right_paren_count = 0
            temp = ""
            if(i == "("):
                temp += i
                left_paren_count += 1
            elif(i == ")"):
                temp += i
                left_paren_count += 1
        elif(i == "("):
            temp += i
            left_paren_count += 1
        elif(i == ")"):
            temp += i
            right_paren_count += 1
    if(temp != ""):
        result.append(temp)
    return result

# print(split("((()))(())()()(()())"))

#Problem 2
# Given a sentence, create a function which shifts the first letter of each word to the next word in the sentence (shifting right).

# Examples
# shift_sentence("create a function") ➞ "freate c aunction"

# shift_sentence("it should shift the sentence") ➞ "st ihould shift she tentence"

# shift_sentence("the output is not very legible") ➞ "lhe tutput os iot nery vegible"

# shift_sentence("edabit") ➞ "edabit"

# Notes
# The last word shifts its first letter to the first word in the sentence.
# All sentences will be given in lowercase.
# Note how single words remain untouched (example #4).

def shift_sentence(s):
    split_s = s.split(" ")
    result = ""
    for i in range(len(split_s)):
        if(i == 0):
            # this will split all the letters in the string and make array of it
            letter_split = [*split_s[i]]
            letter_split[0] = split_s[len(split_s)-1][0]
            result += "".join(letter_split)
            result += " "
        else:
            letter_split = [*split_s[i]]
            letter_split[0] = split_s[i-1][0]
            result += "".join(letter_split)
            if(i != len(split_s)-1):
                result += " "
    return result

# print(shift_sentence("it should shift the sentence"))

