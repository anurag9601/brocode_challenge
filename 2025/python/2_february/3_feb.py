#Using recursion but not that efficient
def productExceptSelf(nums, index=0):
    if(index == len(nums)):
        return []
    current_sum = 1
    for i in range(len(nums)):
        if(i != index):
            current_sum *= nums[i]
    return [current_sum] + productExceptSelf(nums,index + 1)

# print(productExceptSelf([1,2,3,4]))
# print(productExceptSelf([-1,1,0,-3,3]))

#Using prefix suffix 

#Example lst = [1,2,3,4]

#Prefix
# 1
# 1*2
# 1*2*3
# 1*2*3*4

#Suffix
# 4
# 4*3
# 4*3*2
# 4*3*2*1

def productExceptSelfPrefixSuffix(nums):
    n = len(nums)
    result = [1] * n

    #prefix
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1,-1,-1):
        result[i] *= suffix
        suffix *= nums[i]

    return result

# print(productExceptSelfPrefixSuffix([1,2,3,4]))

#Using recursion but not that efficient
def increasingTriplet(nums):
    n = len(nums)
    if(len(nums) < 3):
        return False
    temp_lst = []
    for j in range(n):
        if(len(temp_lst) == 3):
            return True
        elif(temp_lst == []):
            temp_lst.append(nums[j])
        else:
            if(nums[j] > temp_lst[-1]):
                temp_lst.append(nums[j])
            elif(nums[j] < temp_lst[-1] and nums[j] > temp_lst[0]):
                temp_lst[-1] = nums[j]
    if(len(temp_lst) == 3):
        return True
    
    return increasingTriplet(nums[1:])

# print(increasingTriplet([1,2,3,4,5]))
# print(increasingTriplet([5,4,3,2,1]))
# print(increasingTriplet([2,1,5,0,4,6]))
# print(increasingTriplet([1,5,0,4,1,3]))

#Better code

def increasingTriplet(nums):
    first = float('inf')
    second = float('inf')

    for num in nums:
        if num <= first:
            first = num  # Smallest so far
        elif num <= second:
            second = num  # Second smallest
        else:
            return True  # Found a triplet

    return False

# print(increasingTriplet([1,2,3,4,5]))
# print(increasingTriplet([5,4,3,2,1]))
# print(increasingTriplet([2,1,5,0,4,6]))
# print(increasingTriplet([1,5,0,4,1,3]))

def compress(chars):
    chars_lst = []
    for char in chars:
        if char not in chars_lst:
            chars_lst.append(char)
            char_count = 0
            for c in chars:
                if char == c:
                    char_count += 1
            if(char_count > 1):
                for num in str(char_count):
                    chars_lst.append(num)
    return chars_lst
    
# print(compress(["a","a","b","b","c","c","c"]))
# print(compress(["a"]))
# print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))


