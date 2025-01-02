#Problem 1
# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

# Example 1:

# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
# Example 2:

# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.

#Solution
def isPalindrome(s):
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    test_s = ""
    for i in s:
        i = i.lower()
        if(i in alphabet):
            test_s += i
    palindrome_s = ""
    for j in range(len(test_s)-1,-1,-1):
        palindrome_s += test_s[j]
    if(palindrome_s == test_s):
        return True
    else:
        return False
        