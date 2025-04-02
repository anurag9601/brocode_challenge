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

def find_maximum(arr):
    prev = None
    for num in arr:
        if prev and prev > num:
            return prev
        prev = num
    
# print(find_maximum([1, 2, 4, 5, 7, 8, 3]))

#Using recursion
def max_of_subarray(arr, k):
    if len(arr) < k:
            return []
    else:
        max_num = max(arr[:k])
        return [max_num] + max_of_subarray(arr[1:], k)
    
#Without recursion
def max_of_subarray(arr,k):
    if(len(arr) == 1):
            return arr
            
    result = []
    for i in range(len(arr) - (k - 1)):
        result.append(max(arr[i:i+k]))
    return result

    
# print(max_of_subarray([1, 2, 3, 1, 4, 5, 2, 3, 6], 3))
