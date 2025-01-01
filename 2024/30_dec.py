def split(input_str):
    open_paren = 0
    close_paren = 0
    result = []
    temp_s = ""

    for i in input_str:
        if(open_paren != 0 and open_paren == close_paren):
            result.append(temp_s)
            temp_s = ""
            open_paren = 0
            close_paren = 0
        if(i == "("):
            open_paren += 1
            temp_s += i
        if(i == ")"):
            close_paren += 1
            temp_s += i
    result.append(temp_s)
    return result

# print(split("()()()"))
# print(split("((()))(())()()(()())"))
# print(split("((())())(()(()()))"))

def wordPattern(pattern, s):
    lst_s = s.split(" ")

    passed_p = []
    passed_s = []

    if(len(pattern) != len(lst_s)):
        return False
    
    for i in range(len(pattern)):
        for j in range(i,len(pattern)):
            if(pattern[i] == pattern[j]):
                if(lst_s[i] != lst_s[j]):
                    return False
                elif(pattern[i] not in passed_p and lst_s[i] in passed_s):
                    return False
                else:
                    passed_p.append(pattern[i])
                    passed_s.append(lst_s[i])      
    return True

# print(wordPattern("abba", "dog cat cat fish"))
# print(wordPattern("abba", "dog cat cat dog"))

def isAnagram(s, t):
    if(len(t) != len(s)):
            return False

    passed_count = []

    for i in range(len(t)):
        s_count = 0
        t_count = 0
        if(s[i] not in passed_count):
            for j in range(len(t)):
                if(s[i] == s[j]):
                    s_count += 1
                if(s[i] == t[j]):
                    t_count += 1
            if(s_count != t_count):
                return False
            passed_count.append(s[i])
    return True

# print(isAnagram("anagram", "nagaram"))
# print(isAnagram("car", "rat"))

#solving using hash map algorithm
def containsNearbyDuplicate(nums, k):

    hash_index = {}

    for i, num in enumerate(nums):
        if num in hash_index:
            if i - hash_index[num] <= k:
                return True
        hash_index[num] = i
    return False

# print(containsNearbyDuplicate([1,2,3,1], 3))
# print(containsNearbyDuplicate([1,2,3,1,2,3], 2))