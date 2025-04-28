def longestRun(nums):

    longest_run = 1

    temp_long_run = 1

    diff = 1

    for i in range(len(nums) - 1):
        if diff != nums[i + 1] - nums[i]:
            if temp_long_run > longest_run:
                longest_run = temp_long_run
            temp_long_run = 1
            if abs(nums[i + 1] - nums[i]) == 1:
                diff =  nums[i + 1] - nums[i]
                temp_long_run += 1
        else:
            temp_long_run += 1
    return longest_run

# print(longestRun([1, 2, 3, 10, 11, 15]))
# print(longestRun([5, 4, 2, 1]))
# print(longestRun([3, 5, 7, 10, 15]))
print(longestRun([1, 2, 4, 3, 6, 5, 7, 8, 20, 19, 18, 17, 40, 41, 42, 10, 9]))