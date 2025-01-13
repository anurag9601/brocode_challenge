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