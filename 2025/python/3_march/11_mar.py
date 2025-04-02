def subArraySum(arr,target):
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
        
    return [-1]

# print(subArraySum([1, 2, 3, 7, 5], 12))
# print(subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
# print(subArraySum([5, 3, 4], 2))