#Problem 1
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

#Solution
def reverseVowels(self, s):
    """
    :type s: str
    :rtype: str
    """
    s_lst = list(s)
    result = ""
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    present_vowels = []
    count = 0
    for i in range(len(s)):
        if(s[i] in vowels):
            present_vowels.append(s[i])
    for j in range(len(s_lst)-1,-1,-1):
        if(s_lst[j] in vowels):
            s_lst[j] = present_vowels[count]
            count += 1
    for i in s_lst:
        result += i
    return result


#Problem 2
# Given an input string s, reverse the order of the words.

# A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

# Return a string of the words in reverse order concatenated by a single space.

# Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

# Example 1:

# Input: s = "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: s = "  hello world  "
# Output: "world hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: s = "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

#Solution
def reverseWords(self, s):
    """
    :type s: str
    :rtype: str
    """
    temp_lst = []
    temp = ""
    result = ""
    for i in s:
        if(i == " " and temp != ""):
            temp_lst.append(temp)
            temp = ""
        else:
            if(i != " "):
                temp += i
    if(temp != ""):
        temp_lst.append(temp)
        temp = ""
    for i in range(len(temp_lst)-1,-1,-1):
        result += temp_lst[i]
        if(i != 0):
            result += " "
    return result
