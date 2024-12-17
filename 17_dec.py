def find_duplicate(nums):
    result = []

    temp_dict = {}

    for i in nums:
        count = 0
        for j in nums:
            if(i == j):
                count += 1
        temp_dict[i] = count
    
    for key,value in temp_dict.items():
        if(value > 1):
            result.append(key)

    return result

# print(find_duplicate([1, 2, 3, 2, 4, 1]))

#Anagrams are strings where the letters of one string can be rearranged to form the other string, meaning both strings contain the exact same letters in the same frequency.

def are_anagrams(str1, str2):
    passed_i = []

    count = 0

    for i in range(len(str1)):
        for j in range(len(str2)):
            if(str1[i].lower() == str2[j].lower()):
                if(j not in passed_i):
                    count += 1
                    passed_i.append(j)
    if(count == len(str1) and count == len(str2)):
        return True
    else:
        return False

# print(are_anagrams("listen", "silent"))
# print(are_anagrams("Listen", "Silent"))
# print(are_anagrams("a gentleman", "elegant man"))
# print(are_anagrams("rat", "car"))
# print(are_anagrams("school master", "the classroom"))
# print(are_anagrams("", ""))



