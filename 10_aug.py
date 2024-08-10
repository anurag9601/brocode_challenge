# Problem 1
# Given an integer N, return all divisors of N

# Solution 1
def divisors(n):
    all_divisors = []
    for i in range(1,n+1):
        if(n%i == 0):
            all_divisors.append(i)
    return all_divisors


# Problem 2
# Given two integers N1 and N2, find their greatest common
# divisor

# Problem 3
# Given an array, find the occurence of a specific element
# taking input from the user

# Problem 4
# Find index of maximum number of an array  

# Problem 5
# Find index of minimum number of an array
