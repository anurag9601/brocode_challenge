#Problem 1
# A happy number is a number defined by the following process:
# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

# Example 1:
# Input: n = 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1

# Example 2:
# Input: n = 2
# Output: false

#Solution
def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    count = 0
    current = n
    while(count < 10):
        temp = 0
        str_n = str(current)
        for i in str_n:
            temp += int(i)**2
        current = temp
        count += 1
        if(current == 1):
            return True
    return False
            
        