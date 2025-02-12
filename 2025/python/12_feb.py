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

print(find_missing_num([1, 2, 3, 5]))
print(find_missing_num([8, 2, 4, 5, 3, 7, 1]))
print(find_missing_num([1]))



