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

# Solution 2
def same_divisor(n1,n2):
    greatest_divisors = []
    max_num = 0
    if(n1>n2):
        max_num = n1
    else:
        max_num = n2
    for i in range(1, max_num+1):
        if(n1%i==0 and n2%i==0):
            greatest_divisors.append(i)
    return greatest_divisors

# Problem 3
# Given an array, find the occurence of a specific element
# taking input from the user

# Solution 3
def occ_count(lst, element):
    count = 0
    for i in lst:
        if(i==element):
            count += 1
    return count

# Problem 4
# Find index of maximum number of an array  

# Solution 4
def max_num_index(lst):
    index = 0
    max_num = float("-inf")
    for i in range(len(lst)):
        if(lst[i]>max_num):
            max_num = lst[i]
            index = i
    return index


# Problem 5
# Find index of minimum number of an array

# Solution 5
def min_num_index(lst):
    index = 0
    min_num = float("inf")
    for i in range(len(lst)):
        if(lst[i]<min_num):
            min_num = lst[i]
            index = i
    return index

