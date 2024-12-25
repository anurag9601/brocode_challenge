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
    
print(canConstruct("a", "b"))
print(canConstruct("aab", "baa"))