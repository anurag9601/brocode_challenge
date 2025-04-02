def subarray_sum(arr, target):
    if len(arr) == 0:
        return -1

    left = 0
    current_sum = 0

    for right in range(len(arr)):
        if current_sum < target:
            current_sum += arr[right]

        while current_sum > target and left <= right:
            current_sum -= arr[left]
            left += 1

        if current_sum == target:
            return [left + 1, right + 1]
        
    return -1

# print(subarray_sum([1, 2, 3, 7, 5], 12))
# print(subarray_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))


def missing_number(arr):
    expected_n = 1
    for i in range(len(arr)):
        min_i = i
        for j in range(i, len(arr)):
            if arr[min_i] > arr[j]:
                min_i = j
        arr[min_i],arr[i] = arr[i],arr[min_i]
        if arr[i] != expected_n:
            return expected_n
        expected_n = expected_n + 1
    return expected_n

# print(missing_number([1, 2, 3, 5]))
# print(missing_number([8, 2, 4, 5, 3, 7, 1]))
# print(missing_number([1]))

#Able to hand max 3 letters
def permutations(s):
    permutations_lst = []

    for i in range(len(s)):
        char = [*s]
        del char[i]
        for j in range(len(s)):
            itertation_count = 0
            while itertation_count != 2:
                if itertation_count == 1:
                    char = char[::-1]
                char.insert(j, s[i])
                join_char = "".join(char)
                if join_char not in permutations_lst:
                    permutations_lst.append(join_char)
                del char[j]
                itertation_count += 1

    print(len(permutations_lst))
    return " ".join(permutations_lst)


# print(permutations("NOT"))
# print(permutations("AAB"))
# print(permutations("AB"))

def findDuplicates(arr):
    duplicate = []

    for i in range(len(arr) - 1):
        if arr[i] not in duplicates and arr[i] in arr[i+1:]:
            duplicate.append(arr[i])
    
    return duplicate

# print(findDuplicates([2, 3, 1, 2, 3]))
# print(findDuplicates([0, 3, 1, 2]))
# print(findDuplicates([2]))
