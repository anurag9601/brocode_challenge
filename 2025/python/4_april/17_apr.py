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
