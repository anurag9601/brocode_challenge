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