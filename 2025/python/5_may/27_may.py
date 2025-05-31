def cutting_grass(*args):
    grass_l = args[0]
    cut_l = list(args[1:])

    result = []

    for cut in cut_l:
        if 0 in grass_l:
            result.append("Done")
        else:
            for i in range(len(grass_l)):
                grass_l[i] = grass_l[i] - cut
            if 0 not in grass_l:
                copy_grass_l = grass_l.copy()
                result.append(copy_grass_l)
            else:
                result.append("Done")
    return result

# print(cutting_grass([4, 4, 4, 4], 1, 1, 1, 1))
# print(cutting_grass([5, 6, 7, 5], 1, 2, 1))
# print(cutting_grass([1, 0, 1, 1], 1, 1, 1))

# Write a function that makes the first number as large as possible by swapping out its digits for digits in the second number.
def num_to_listnum(num):
    result = []
    while(num != 0):
        last_num = num % 10
        num = num // 10
        result.insert(0, last_num)
    return result

def max_possible(n1, n2, fn):
    list_n1 = fn(n1)
    list_n2 = sorted(fn(n2), reverse=True)
    result = 0
    n2_index = 0
    for i in range(len(list_n1)):
        if n2_index < len(list_n2) and list_n1[i] < list_n2[n2_index]:
            list_n1[i] = list_n2[n2_index]
            n2_index += 1
        result = result * 10 + list_n1[i]
    
    return result

# print(max_possible(523, 76, num_to_listnum))
# print(max_possible(9132, 5564, num_to_listnum))
# print(max_possible(8732, 91255, num_to_listnum))