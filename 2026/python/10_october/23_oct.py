def bitwise_index(nums):
    if len(nums) == 0:
        return "The list is empty."
    
    [highest_num, num_index] = [float("-inf"), -1]

    def is_even(n):
        return not (n & 1)

    for i in range(len(nums)):
        if nums[i] > highest_num and is_even(nums[i]) == True and is_even(i) == True :
            highest_num = nums[i]
            num_index = i

    if highest_num >= 0 and is_even(highest_num) == is_even(num_index):
        return {f"@even index {num_index}":  highest_num }
    else:
        return "No even integer found!"

# print(bitwise_index([107, 19, 36, -18, -78, 24, 97]))
# print(bitwise_index([31, 7, 2, 13, 7, 9, 10, 13]))
# print(bitwise_index([4, 4, 4, 4, 4, 4]))
# print(bitwise_index([-31, -7, -13, -7, -9, -13]))


