def majorityElement(num_arr):
    half_len_arr = round(len(num_arr) / 2)

    passed_num = []

    for num in num_arr:
        if num not in passed_num:
            passed_num.append(num)
            remove_ele = num
            filter_lst = list(filter(lambda x: x != remove_ele, num_arr))
            occurence = len(num_arr) - len(filter_lst)
            if occurence > half_len_arr:
                return num 
    return -1

# print(majorityElement([3, 1, 3, 3, 2]))
# print(majorityElement([7]))
# print(majorityElement([2, 13]))

def maxSumArraySum(arr):
    if len(arr) == 1:
        return arr[0]

    max_sum = float("-inf")

    current_sum = 0

    for num in arr:
        current_sum += num

        max_sum = max(max_sum, current_sum)

        if current_sum < 0:
            current_sum = 0

    return max_sum

print(maxSumArraySum([-5,-6,-3,-2]))