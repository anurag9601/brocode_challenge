#Problem 1
# There are two players, Alice and Bob, each with a 3-by-3 grid. A referee tells Alice to fill out one particular row in the grid (say the second row) by putting either a 1 or a 0 in each box, such that the sum of the numbers in that row is odd. The referee tells Bob to fill out one column in the grid (say the first column) by putting either a 1 or a 0 in each box, such that the sum of the numbers in that column is even.

# Alice and Bob win the game if Alice’s numbers give an odd sum, Bob’s give an even sum, and (most important) they’ve each written down the same number in the one square where their row and column intersect.

#Solution
def magic_square_game(alice_choice, bob_choice):
    if(alice_choice[1][bob_choice[0]-1] == bob_choice[1][alice_choice[0]-1]):
        return True
    else:
        return False

#Examples
# print(magic_square_game([2, "100"], [1, "101"]))
# print(magic_square_game([2, "001"], [1, "101"]))
# print(magic_square_game([3, "111"], [2, "011"]))
# print(magic_square_game([1, "010"], [3, "101"]))

#Problem2
# Your goal is to create a function that returns a list with a string for each of the 108 tiles in the following format:

# "rank suit"
# Where rank is a number from 1 to 9 and suit is one of the three suits (tong, tiao, wan), both written in the pinyin transcription of Mandarin Chinese (for numbers see table below).

# Number	Character	Pinyin
# 1	一	yi
# 2	二	er
# 3	三	san
# 4	四	si
# 5	五	wu
# 6	六	liu
# 7	七	qi
# 8	八	ba
# 9	九	jiu
# Three of the tiles have special names. Each of the 4 copies of these tiles should be represented by their names only (no suit, no rank):

# One of tong is called bing gan (饼干, cookie)
# Two of tong is called yan jing (眼镜, glasses)
# One of tiao is called ji (鸡, chicken)

# Examples of tiles
# Five of tong ➞ "wu tong"

# Seven of wan ➞ "qi wan"

# One of tiao ➞ "ji"

# Three of tiao ➞ "san tiao"

#Solution
def get_tile_name(str):
    other_char_lst = [["One","yi"],["Two","er"],["Three","san"],["Four","si"],["Five","wu"],["Six","liu"],["Seven","qi"],["Eight","ba"],["Nine","jiu"]]
    split_str = str.split(" ")
    if(split_str[0] == "One" and split_str[2] == "tong"):
        return  "bing gan"
    elif(split_str[0] == "One" and split_str[2] == "tiao"):
        return "ji"
    elif(split_str[0] == "Two" and split_str[2] == "tong"):
        return "yan jing"
    else:
        for i in other_char_lst:
            if(i[0] == split_str[0]):
                split_str[0] = i[1]
                result = ''
                for i in split_str:
                    result += i
                    result += " "
                return result
        return "Result not found"

#Examples
print(get_tile_name("Five of tong"))
print(get_tile_name("Seven of wan"))
print(get_tile_name("One of tiao"))

