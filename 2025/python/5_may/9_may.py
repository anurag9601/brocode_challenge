def factor_sort(nums):
    factor_dict = {}
    result = []
    for num in nums:
        factor_count = 0
        for i in range(1,num + 1):
            if num % i == 0:
                factor_count += 1
        factor_dict[num] = factor_count
print(factor_sort([9, 7, 13, 12]))

