# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
# Constraints
# Each character in the string is an ascii character.
# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string.
# Sample Input

def count_substring(string, sub_string):
    occur_c = 0
    for i in range((len(string) - (len(sub_string) - 1))):
        curr_i = 0
        for j in range(i, len(string)):
            if string[j] != sub_string[curr_i]:
                break
            elif string[j] == sub_string[curr_i]:
                curr_i += 1
                if curr_i == len(sub_string):
                    occur_c += 1
                    break
    return occur_c

# if __name__ == '__main__':
    # string = input().strip()
    # sub_string = input().strip()
    
    # count = count_substring(string, sub_string)
    # print(count)

# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

def threeSum(nums):
    if len(nums) < 3:
        return -1
    
    result = []
    nums.sort()

    for i,a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l , r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]

            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                if [a, nums[l], nums[r]] not in result:
                    result.append([a, nums[l], nums[r]])
                l += 1
    return result

# print(threeSum([-1,0,1,2,-1,-4]))

def stair(n):

    if n == 0:
        return "___"
    
    spaces = n * 2
    result = ""

    while(spaces != 0):
        if spaces == n * 2:
            result += " " * spaces + "_" + "\n"
        else:
            result += " " * spaces + "_" + "|" + "\n"
        spaces -= 2
    
    result += "_" + "|"

    return result

# print(stair(3))
# print(stair(4))
# print(stair(10))

# Python has built-in string validation methods for basic data. It can check if a string is composed of alphabetical characters, alphanumeric characters, digits, etc.

# str.isalnum()
# This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).

# if __name__ == '__main__':
    # s = input()
    
    # isAlphaNumeric = False
    # isHasAnyAlpha = False
    # isHasAnyDigit = False
    # isHasAnyLower = False
    # isHasAnyUpper = False
    
    # for char in s:
    #     if char.isalnum():
    #         isAlphaNumeric = True
    #     if char.isalpha():
    #         isHasAnyAlpha = True
    #     if char.isdigit():
    #         isHasAnyDigit = True
    #     if char.islower():
    #         isHasAnyLower = True
    #     if char.isupper():
    #         isHasAnyUpper = True
        
    # print(isAlphaNumeric)
    # print(isHasAnyAlpha)
    # print(isHasAnyDigit)
    # print(isHasAnyLower)
    # print(isHasAnyUpper)

# 16. 3Sum Closest
# Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
# Example 1:
# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).

def threeSumClosest(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    close_sum = 0
    difference = float("inf")
    nums.sort()

    for i,a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue
        l , r = i + 1, len(nums) - 1
        while l < r:
            threeSum = a + nums[l] + nums[r]
            if abs(threeSum - target) < difference:
                close_sum = threeSum
                difference = abs(threeSum - target)
            if threeSum < target:
                l += 1
            elif threeSum > target:
                r -= 1
            else:
                l += 1
    return close_sum

# Create a function that takes a string and returns the reversed string. However there's a few rules to follow in order to make the challenge interesting:
# The UPPERCASE/lowercase positions must be kept in the same order as the original string (see example #1 and #2).
# Spaces must be kept in the same order as the original string (see example #3).
# Examples
# special_reverse_string("Edabit") ➞ "Tibade"
# special_reverse_string("UPPER lower") ➞ "REWOL reppu"
# special_reverse_string("1 23 456") ➞ "6 54 321"

def special_reverse_string(s):
    result = ""
    reverse_char = "".join("".join(list(reversed(s))).split(" "))
    index = 0
    
    for char in s:
        if char == " ":
            result += " "
        elif char.isupper():
            result += reverse_char[index].upper()
            index += 1
        elif char.islower():
            result += reverse_char[index].lower()
            index += 1
        else:
            result += reverse_char[index]
            index += 1
    
    return result

# print(special_reverse_string("UPPER lower"))
# print(special_reverse_string("Edabit"))
# print(special_reverse_string("1 23 456"))


