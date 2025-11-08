def freq_count(num_list, ele, sub_list_count=0):
    present_ele_count = 0

    for i in range(len(num_list)):
        if isinstance(num_list[i], list):
            return freq_count(num_list[i], ele, sub_list_count + 1)
        elif isinstance(num_list[i], int) and num_list[i] == ele:
            present_ele_count += 1
    return [sub_list_count, present_ele_count]

# print(freq_count([1, 4, 4, [1, 1, [1, 2, 1, 1]]], 1))
# print(freq_count([1, 5, 5, [5, [1, 2, 1, 1], 5, 5], 5, [5]], 5))
# print(freq_count([1, [2], 1, [[2]], 1, [[[2]]], 1, [[[[2]]]]], 2))

