def gcd(a, b):
    while b:
        a , b = b , a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)  #formula LCM(a,b)= a×b / GCD(a,b)

def list_of_lcm(nums):
    result = nums[0]
    for num in nums[1:]:
        result = lcm(result, num)
    return result

# print(lcm(4,80))
# print(list_lcm([5, 7, 11, 35, 55, 77]))
# print(list_lcm([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def authentic_skewer(str):
    str = str.lower()
    vowels = 'aeiou'
    consonents = 'bcdfghjklmnopqrstvwxyz'
    find_min_space = False
    min_space = 0
    current_space = 0
    vowel_turn = False

    for i in range(len(str)):
        if str[i] in vowels or str[i] in consonents:
            if i != 0 and not find_min_space:
                find_min_space = True
            if str[i] in vowels and not vowel_turn:
                return False
            if str[i] in consonents and vowel_turn == True:
                return False
            if i == len(str) - 1 and vowel_turn == True:
                return False
            vowel_turn = not vowel_turn
            current_space = 0
        else:
            if i == 0:
                return False
            if not find_min_space:
                min_space += 1
            current_space += 1
            if current_space > min_space:
                return False
    return True

# print(authentic_skewer("B--A--N--A--N--A--S"))
# print(authentic_skewer("A--X--E"))
# print(authentic_skewer("M--A---T-E-S"))
# print(authentic_skewer("C-L-A-P"))
            
