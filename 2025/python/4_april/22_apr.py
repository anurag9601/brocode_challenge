def compress(chars):
    if len(chars) == 1:
        return chars[0]
        
    result = ""
    
    char_c = 1
    for i in range(len(chars) - 1):
        if chars[i] != chars[i+1]:
            if char_c > 1:
                result += f"{chars[i]}{char_c}"
            else:
                result += chars[i]
            char_c = 1
        elif chars[i] == chars[i+1]:
            char_c += 1
    if char_c > 1:
        result += f"{chars[-1]}{char_c}"
    else:
        result += chars[-1]
    
    return result
    
# print(compress(["a", "a", "b", "b", "c", "c", "c"]))
# print(compress(["a", "b"]))
# print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
# print(compress(["a", "a", "a", "b", "b", "a", "a"]))

# Split 25 (Part 1)
# About a month ago I stumbled upon an interesting problem — something called the 25 split. In the problem, you had to break up 25 into parts that add to it, and, from those parts, try to create the biggest product.
# For example, 3 * 22 = 66 or 5 * 5 * 5 * 5 * 5 = 3125. With this first part, return the value of the biggest product possible using natural number parts from a given number, x.

def split(n):
    #if n if less than or equal to 3
    # example 2 -> 1 + 1 but 1 * 1 -> 1 so 2 will be biggest product
    # example 3 -> 2 + 1 -> 2 * 1 -> 2 so only 3 because it will be biggest product
    if n <= 3:
        return n
    # example 9 -> 3 + 3 + 3 -> 9 and 3 * 3 * 3 -> 27 will be the biggest product of 9
    if n % 3 == 0:
        return 3 ** (n // 3)
    # example 10 -> 3 + 3 + 3 + 1 -> 3 * 3 * 3 * 1 -> 27 so in this case 1 is useless but if we will do 3 + 3 + 4 -> 3 * 3 * 4 -> 36 so now we are getting more higher number than before so for this case
    if n % 3 == 1:
        return 3 ** ((n // 3) - 1) * 4
    # example 17 -> 17 // 3 -> 5 because 3 * 5 -> 15 remaining 2 so the sequence will be 3 + 3 + 3 + 3 + 3 + 2
    else:
        return 3 ** (n // 3) * 2
    
# print(split(25))
# print(split(1))
# print(split(10))
# print(split(5))

# 200. Number of Islands
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

def numIslands(grid):
    r, c = len(grid), len(grid[0])

    islands = 0

    def dfs(i, j): #dfs stands for depth first search
        if i < 0 or i >= r or j < 0 or j >= c or grid[i][j] != "1":
            return
        else:
            grid[i][j] = "0"
            dfs(i , j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)


    for i in range(r):
        for j in range(c):
            if grid[i][j] == "1":
                islands += 1
                dfs(i , j)
    
    return islands

# print(numIslands([
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]))

def split_into_buckets(s, max_length):
    result = []
    split_s = s.split(" ")

    i = 0
    temp_s = ""
    while i < len(split_s):
        if len(temp_s) == 0:
            temp_s += split_s[i]
            i += 1
        elif (len(temp_s) + 1 + len(split_s[i])) <= max_length:
            temp_s += " "
            temp_s += split_s[i]
            i += 1
        if i >= (len(split_s) - 1) or (len(temp_s) + 1 + len(split_s[i])) > max_length:
            result.append(temp_s)
            temp_s = ""
    return result

# print(split_into_buckets("she sells sea shells by the sea", 10))
# print(split_into_buckets("the mouse jumped over the cheese", 7))
# print(split_into_buckets("fairy dust coated the air", 20))
# print(split_into_buckets("a b c d e", 2))

# 12. Integer to Roman

# Example 1:
# Input: num = 3749
# Output: "MMMDCCXLIX"
# Explanation:
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
#  700 = DCC as 500 (D) + 100 (C) + 100 (C)
#   40 = XL as 10 (X) less of 50 (L)
#    9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

# Example 2:
# Input: num = 58
# Output: "LVIII"
# Explanation:
# 50 = L
#  8 = VIII

# Example 3:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation:
# 1000 = M
#  900 = CM
#   90 = XC
#    4 = IV
 

def intToRoman(self, num):
    """
    :type num: int
    :rtype: str
    """
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    romanLetters = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    roman = ""

    for i in range(len(values)):
        while num >= values[i]:
            roman = roman + romanLetters[i]
            num = num - values[i]
    
    return roman
    