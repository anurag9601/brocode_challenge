# Daily codebro assignment

# Problem 1
# Given an integer N, return true it is an Armstrong number otherwise return false.
# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.

# Problem 2
# Given an integer N, return the number of digits in N.

# Problem 3 
# Given an integer N (NOT STRING), return true if it is a palindrome else return false.

# Problem 4
# Given an integer N, check whether it is prime or not. A prime number is a number that is only divisible by 1 and itself and the total number of divisors is 2.

# Problem 5
# If we list all the natural numbers below 10 that are multiples of
# 3 or 5, we get 3, 5, 6, 9. The sum of these multiples is 23. Find
# the sum of all the multiples of 3 or 5 below 1000.


#Problem 1
def isArmstrong(n):
    str_n = str(n)
    raise_n = len(str_n)
    sum = 0
    for i in str_n:
        sum += int(i)**raise_n
    return sum == n


#Problem 2
def digit_n(n):
    return f"Number of digits are {len(str(n))}"


#Problem 3
def isPalindrome_n(n):
    return str(n)[::-1] == str(n)


#Problem 4
def isPrime_n(n):
    if(n == 0 or n == 1):
        return "Not prime"
    else:
        for i in range(2, n):
            if(n%i == 0):
                return "Not prime"
        else:
            return "Prime"


#Prime 5
def sum_of_multi(n1,n2):
    range_n = int(input("Range of the loop: "))
    result = 0
    min = 0
    if(n1<n2):
        min = n1
    else:
        min = n2
    for i in range(min, range_n):
        if(i%n1 == 0 or i%n2 == 0):
            result += i
    return f"The sum of all the multiples of {n1} or {n2} below {range_n} is {result}"

