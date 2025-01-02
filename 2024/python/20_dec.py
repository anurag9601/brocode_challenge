def can_see_stage(lst):
    for i in range(len(lst[0])):
        for j in range(len(lst)-1):
            if(lst[i][j] > lst[i][j+1]):
                return False
    return True

# print(can_see_stage([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]))
# print(can_see_stage([
#   [1, 0, 0],
#   [1, 1, 1],
#   [2, 2, 2]
# ]))
# print(can_see_stage([
#   [0, 0, 0],
#   [1, 1, 1],
#   [2, 2, 2]
# ]))

def shift_setence(input_str):
    split_input_str = input_str.split(" ")
    current_first_letter = split_input_str[0][0]
    for i in range(1,len(split_input_str)+1):
        if(i == len(split_input_str)):
            i = 0
        split_word = [*split_input_str[i]]
        words_first_letter = split_word[0]
        split_word[0] = current_first_letter
        split_word = "".join(split_word)
        split_input_str[i] = split_word
        current_first_letter = words_first_letter
    return " ".join(split_input_str)
    

# print(shift_setence("create a function"))
# print(shift_setence("it should shift the sentence"))
# print(shift_setence("Awesome"))

def advanced_sort(lst):
    result = []
    for i in lst:
        already_created = False
        for j in result:
            if(i in j):
                already_created = True
                j.append(i)
                break
        if(already_created == False):
            temp = []
            temp.append(i)
            result.append(temp)
    return result

# print(advanced_sort([2, 1, 2, 1]))
# print(advanced_sort([5, 4, 5, 5, 4, 3]))
# print(advanced_sort(["b", "a", "b", "a", "c"]))

#Problem 
# A numbers factor length is simply its total number of factors.
# For instance:

# 3: 1, 3
# # 3's factor length = 2

# 8: 1, 2, 4, 8
# # 8's factor length = 4

# 36 : 1, 2, 3, 4, 6, 9, 12, 18, 36
# # 36's factor length = 9
# Create a function that sorts a list by factor length in descending order. If multiple numbers have the same factor length, sort these numbers in descending order, with the largest first.

# In the example below, since 13 and 7 both have only 2 factors, we put 13 ahead of 7.

# factor_sort([9, 7, 13, 12]) ➞ [12, 9, 13, 7]
# 12 : 6, 9: 3, 13: 2, 7: 2

def factor_sort(num_lst):
    factorial_len_lst = []
    for num in num_lst:
        factorial_count = 0
        for i in range(1,num+1):
            if(num%i == 0):
                factorial_count = factorial_count + 1
        factorial_len_lst.append(factorial_count)
    
    for i in range(len(factorial_len_lst)):
        max_i = i
        for j in range(i, len(factorial_len_lst)):
            if(factorial_len_lst[max_i] == factorial_len_lst[j]):
                if(num_lst[max_i] < num_lst[j]):
                    max_i = j
            elif(factorial_len_lst[max_i] < factorial_len_lst[j]):
                max_i = j
        factorial_len_lst[i],factorial_len_lst[max_i] = factorial_len_lst[max_i],factorial_len_lst[i]
        num_lst[i],num_lst[max_i] = num_lst[max_i],num_lst[i]
    return num_lst

# print(factor_sort([5, 7, 9]))
# print(factor_sort([1, 2, 31, 4]))
# print(factor_sort([15, 8, 2, 3]))

# 1. Two Sum Problem:
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.   
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#Solution
def two_sum_problem(num_lst, target):
    for i in range(len(num_lst)-1):
        for j in range(i+1, len(num_lst)):
            current_sum = num_lst[i] + num_lst[j]
            if(current_sum == target):
                return [i,j]

def two_sum(num_lst, target):
    left = 0
    right = len(num_lst) - 1

    while left < right:
        current_sum = num_lst[left] + num_lst[right]

        if current_sum == target:
            return [left, right]
        elif current_sum > target:
            right -= 1
        else:
            left += 1

# print(two_sum_problem([2,7,11,15], 9))

# print(two_sum([2,7,11,15], 9))
# print(two_sum([1, 3, 5, 7, 9], 12))
# print(two_sum(list(range(1, 10001)), 19999))

# 2. Best Time to Buy and Sell Stock:
# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.   
# Example:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

def best_time_to_Buy_stock(stock_lst):
    maximum_profit = 0
    buy_price = 0
    sell_price = 0
    for i in range(len(stock_lst) - 1):
        current_stock_price = stock_lst[i]
        for j in range(i+1, len(stock_lst)):
            if(current_stock_price < stock_lst[j]):
                current_profit = stock_lst[j] - current_stock_price
                if(current_profit > maximum_profit):
                    maximum_profit = current_profit
                    buy_price = current_stock_price
                    sell_price = stock_lst[j]
    print(f"Buy price:- {buy_price}")
    print(f"Sell price:- {sell_price}")
    return f"Profit {maximum_profit}"

# print(best_time_to_Buy_stock([7,1,5,3,6,4]))
# print(best_time_to_Buy_stock([7,6,4,3,1]))
# print(best_time_to_Buy_stock([1,2,3,4,5]))

# 3. Merge Sorted Arrays:
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into one sorted array, modifying nums1 in-place. The number of elements in nums1 will be m + n. You may assume the nums1 has enough space (size that is equal to m + n) to hold additional elements from nums2.   
# Example:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

def merge_sorted_array(nums1, nums2, m , n):
    i_count = n-1
    for i in range(len(nums1)-1, -1, -1):
        if(i == m-1):
            break
        else:
            nums1[i] = nums2[i_count]
            i_count = i_count - 1
    for i in range(len(nums1)):
        min_i = i
        for j in range(i, len(nums1)):
            if(nums1[min_i] > nums1[j]):
                min_i = j
        nums1[min_i],nums1[i] = nums1[i],nums1[min_i]
    return nums1

# print(merge_sorted_array([1,2,3,0,0,0],[2,5,6],3,3))