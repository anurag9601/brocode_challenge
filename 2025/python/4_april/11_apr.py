def advance_sort(num_lst):
    ele_i = {}
    result = []
    index_count = 0
    for num in num_lst:
        if num in ele_i.keys():
            result[ele_i[num]].append(num)
        else:
            ele_i[num] = index_count
            index_count += 1
            result.append([num])
    return result

# print(advance_sort([2, 1, 2, 1]))
# print(advance_sort(["b", "a", "b", "a", "c"]))

