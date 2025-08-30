def find_missing_number(nums):
    sorted_lst = sorted(nums)
    expected_n = sorted_lst[0]
    for num in sorted_lst:
        if expected_n != num:
            return expected_n
        else:
            expected_n += 1
    return "All numbers are present"

# print(find_missing_number([3, 0, 1]))

def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        cur_sum = nums[left] + nums[right]

        if cur_sum == target:
            return [left, right]

        if cur_sum > target:
            right -= 1
        elif cur_sum < target:
            left += 1
        else:
            left += 1
    return "No target sum found in the list"

# print(two_sum([2, 7, 11, 15], 9))