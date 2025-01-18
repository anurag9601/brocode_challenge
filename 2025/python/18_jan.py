def is_disarium(n):
    total = 0
    str_n = str(n)
    for i in range(len(str_n)):
        total += int(str_n[i]) ** (i + 1)
    return True if n == total else False

# print(is_disarium(75))
# print(is_disarium(135))
# print(is_disarium(544))
# print(is_disarium(518))
# print(is_disarium(466))
# print(is_disarium(8))

def consecutive_combo(lst1, lst2):
    merge_lst = lst1 + lst2

    for i in range(len(merge_lst)):
        mini_i = i
        for j in range(i, len(merge_lst)):
            if(merge_lst[mini_i] > merge_lst[j]):
                mini_i = j
        merge_lst[i],merge_lst[mini_i] = merge_lst[mini_i],merge_lst[i]
    
    for num in range(merge_lst[0], merge_lst[-1]+1):
        if(num not in merge_lst):
            return False

    return True

# print(consecutive_combo([7, 4, 5, 1], [2, 3, 6]))
# print(consecutive_combo([1, 4, 6, 5], [2, 7, 8, 9]))
# print(consecutive_combo([1, 4, 5, 6], [2, 3, 7, 8, 10]))
# print(consecutive_combo([44, 46], [45]))

