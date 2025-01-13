def double_factorial(n, count=1):
    if(n == 0 or n == 1):
        return n
    if(count % 2 != 0):
        return n * double_factorial(n-1, count=count+1)
    else:
        return double_factorial(n - 1, count=count+1)

# print(double_factorial(0))
# print(double_factorial(2))
# print(double_factorial(9))
# print(double_factorial(14))

def sum_list(input_lst):
    total = 0
    for item in input_lst:
        if isinstance(item, list):
            total += sum_list(item)
        else:
            total += item
    return total

# print(sum_list([1, 2, 3]))
# print(sum_list([1, [2, [1]], 3]))

def largest_even(input_lst, max_even=-1):
    if not input_lst:
        return max_even

    if input_lst[0] % 2 == 0 and input_lst[0] > max_even:
        max_even = input_lst[0]
    return largest_even(input_lst[1:], max_even)


# print(largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
# print(largest_even([1, 3, 5, 7]))