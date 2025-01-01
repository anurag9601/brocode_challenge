def canConstruct(ransomNote, magazine):
    passed_i = []
    count = 0

    for i in range(len(ransomNote)):
        for j in range(len(magazine)):
            if(ransomNote[i] == magazine[j] and j not in passed_i):
                count += 1
                passed_i.append(j)
                break
    if(count == len(ransomNote)):
        return True
    else:
        return False
    
# print(canConstruct("a", "b"))
# print(canConstruct("aab", "baa"))

def simplify(input_str):
    split_input_str = input_str.split("/")
    first_int = int(split_input_str[0])
    second_int = int(split_input_str[1])
    k = first_int if first_int < second_int else second_int

    result = []

    for i in range(2, k + 1):
        if(first_int%i == 0 and second_int%i == 0):
            result = []
            result.append(str(first_int//i))
            result.append(str(second_int//i))
        
    return input_str if result == [] else "/".join(result)

# print(simplify("4/6"))
# print(simplify("100/400"))
# print(simplify("8/4"))
# print(simplify("10/11"))