# 1. Remove Duplicates from Sorted Array
# Description: Given a sorted array, remove duplicate elements in-place such that each element appears only once and return the new length.
# Example: Input: [1,1,2] Output: 2, array is modified to [1,2,_]

# 2. Find the Missing Number
# Description: Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.   
# Example: Input: [3,0,1] Output: 2   

# 3. Merge Two Sorted Arrays
# Description: Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# Example: Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 Output: [1,2,2,3,5,6]   

# 4. Find the First Non-Repeating Character
# Description: Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.
# Example: Input: "leetcode" Output: 0   

# 5. Check for Anagrams
# Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# Example: Input: s = "anagram", t = "nagaram" Output: true

#Problem 1
#I think this code is not reacting as per the question
def remove_dupli(lst):
    temp_l = []
    for i in range(len(lst)):
        if(lst[i] not in temp_l):
            temp_l.append(lst[i])
    return len(temp_l)


#Problem 2
def find_missing_num(lst):
    minimum = float("inf")
    maximum = float("-inf")
    for i in lst:
        if(minimum > i):
            minimum = i
    for j in lst:
        if(maximum < j):
            maximum = j
    for k in range(minimum, maximum + 1):
        if(k not in lst):
            return k



  

