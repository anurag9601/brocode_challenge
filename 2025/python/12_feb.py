def find_missing_num(input_arr):
    current_check = None
    for i in range(len(input_arr)):
        mini = i
        for j in range(i, len(input_arr)):
            if input_arr[mini] > input_arr[j]:
                mini = j
        input_arr[mini],input_arr[i] = input_arr[i],input_arr[mini]
        if not current_check:
            current_check = input_arr[i] + 1
        else:
            if input_arr[i] == current_check:
                current_check = input_arr[i] + 1
            else:
                return current_check
    return current_check

# print(find_missing_num([1, 2, 3, 5]))
# print(find_missing_num([8, 2, 4, 5, 3, 7, 1]))
# print(find_missing_num([1]))


def kadenes_algo(num_arr):
    max_sum = float("-inf")
    for i in range(len(num_arr)):
        current_sum = 0
        for j in range(i, len(num_arr)):
            current_sum += num_arr[j]
            if(current_sum > max_sum):
                max_sum = current_sum
    return max_sum

# print(kadenes_algo([2, 3, -8, 7, -1, 2, 3]))
# print(kadenes_algo([-2, -4]))
# print(kadenes_algo([5, 4, 1, 7, 8]))

def second_largest(arr):
    # modify_arr = sorted(list(set(arr)))
    modify_arr = list(set(arr))
    for i in range(len(modify_arr)):
        mini_i = i
        for j in range(i, len(modify_arr)):
            if(modify_arr[mini_i] > modify_arr[j]):
                mini_i = j
        modify_arr[mini_i], modify_arr[i] = modify_arr[i],modify_arr[mini_i]
    return modify_arr[-2] if len(modify_arr) > 1 else -1

# print(second_largest([12, 35, 1, 10, 34, 1]))
# print(second_largest([10, 5, 10]))
# print(second_largest([10, 10, 10]))

def arr_leader(arr):
    result = []
    for i in range(len(arr)):
        current_i_sort = sorted(arr[i:])
        if current_i_sort[-1] == arr[i]:
            result.append(arr[i])
    return result

# print(arr_leader([16, 17, 4, 3, 5, 2]))
# print(arr_leader([10, 4, 2, 4, 1]))
# print(arr_leader([5, 10, 20, 40]))
# print(arr_leader([30, 10, 10, 5]))
                



