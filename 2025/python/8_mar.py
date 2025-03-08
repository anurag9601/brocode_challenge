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