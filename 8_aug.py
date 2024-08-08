# Problem 1
# Print Name N times using Recursion in python
# Example: function("hrisabhy", 3)
# Output:
# hrisabhy
# hrisabhy
# hrisabhy

# Problem 2
# Print 1 to N using Recursion
# Example: print_numbers(5)
# Output:
# 1
# 2
# 3
# 4
# 5

# Problem 3 Print N to 1 using Recursion

# Problem 4 Sum of First N Natural Numbers

# Problem 5 Calculate Factorial of N


#Problem 1
def n_print(string, range_n):
    if(range_n <= 0):
        return ""
    else:
        return string + "\n" + n_print(string, range_n - 1)


#Problem 2
#this is not correct code because when we are printing then it returns none at the end
def num_print(n ,current = 1):
    if(current > n):
        return 
    print(current)
    num_print(n, current + 1)
  

#Problem 3
#same correction
def num_revers(n):
    if(n <= 0):
        return 
    else:
        print(n)
        num_revers(n-1)

#Problem 4
def sum_n(n):
    if(n == 0):
        return 0
    else:
        return n + sum_n(n - 1)

#Problem 5
def factorial(n):
    if(n == 0):
        return 1
    else:
        return n * factorial(n - 1)
