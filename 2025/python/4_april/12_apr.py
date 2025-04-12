#Hackerrank tuple problem
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    # print(hash(t))

# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
# For Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2 

def swap_case(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    split_s = [*s]
    for i in range(len(split_s)):
        small_char = split_s[i].lower()
        if small_char in alpha:
            if small_char == split_s[i]:
                split_s[i] = split_s[i].upper()
            else:
                split_s[i] = split_s[i].lower()
    return "".join(split_s)
                
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    # print(result)

# In Python, a string can be split on a delimiter.
# Example:
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings. 
# >>> print a
# ['this', 'is', 'a', 'string']

def split_and_join(line):
    # write your code here
    split_l = line.split(" ")
    return "-".join(split_l)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    # print(result)

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:
# Hello firstname lastname! You just delved into python.
# Function Description
# Complete the print_full_name function in the editor below.
# print_full_name has the following parameters:
# string first: the first name
# string last: the last name

def print_full_name(first, last):
    # Write your code here
    print(f"Hello {first} {last}! You just delved into python.")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    # print_full_name(first_name, last_name)