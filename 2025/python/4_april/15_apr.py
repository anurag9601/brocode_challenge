# Consider the following:

# A string, , of length  where .
# An integer, , where  is a factor of .
# We can split  into  substrings where each subtring, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

# The characters in  are a subsequence of the characters in .
# Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
# Given  and , print  lines where each line  denotes string .

def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        temp_s = ""
        for char in string[i:i+k]:
            if char not in temp_s:
                temp_s += char
        print(temp_s)
if __name__ == '__main__':
    string, k = input(), int(input())
    # merge_the_tools(string, k)

# collections.Counter()
# A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.

# Sample Code

# >>> from collections import Counter
# >>> 
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>> 
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]

from collections import Counter

pice_n = int(input())
stock = list(map(int, input().split(" ")))
x = int(input())
dict = Counter(stock)
total = 0

for i in range(x):
    size,price = map(int, input().split(" "))
    
    if dict[size]:
        dict[size] -= 1
        total += price
# print(total)