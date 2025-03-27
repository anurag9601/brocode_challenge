def search(arr, x):
    return arr.index(x) if x in arr else -1

# print(search([1, 2, 3, 4], 3))

def get_min_max(arr):
    min = float("inf")
    max = float("-inf")

    for num in arr:
        if min > num:
            min = num
        if max < num:
            max = num

    return min, max

# print(get_min_max([3, 2, 1, 56, 10000, 167]))

def convert_to_wave(arr):
    for i in range(1, len(arr), 2):
        current_num = arr[i]
        arr[i] = arr[i - 1]
        arr[i - 1] = current_num
    return arr

# print(convert_to_wave([1, 2, 3, 4, 5]))
