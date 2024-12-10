def is_match(s, p):
    count = 0

    passed_s = []

    if(p == ".*"):
        #Because this expression accepts all strings but not a number
        for i in s:
            try:
                int(i)
            except:
                count += 1
        if(count == len(s)):
            return True
        else:
            return False
    elif(p == "a*z"):
        for i in s:
            lower_case = i.lower()
            if(lower_case == i):
                count += 1
        if(count == len(s)):
            return True
        else:
            return False
    elif(p == "A*Z"):
        for i in s:
            upper_case = i.upper()
            if(upper_case == i):
                count += 1
        if(count == len(s)):
            return True
        else:
            return False
    elif(p == "a*zA*Z"):
        for i in s:
            try:
                int(i)
            except:
                count += 1
        if(count == len(s)):
            return True
        else:
            return False
    elif(p == "1*9"):
        string_int = str(s)
        for i in string_int:
            try:
                int(i)
                count += 1
            except:
                None
        if(count == len(string_int)):
            return True
        else:
            return False
    else:
        for i in s:
            for j in range(len(p)):
                if(i == p[j]):
                    if( i not in passed_s):
                        passed_s.append(i)
                        count += 1
                    elif(i in passed_s and j != len(p)-1):
                        if(p[j+1] == "*"):
                            count += 1
        if(count == len(s)):
            return True
        else:
            return False

def advanced_sort(lst):
    result = []

    added_elements = []

    for i in lst:
        temp = []
        if(i not in added_elements):
            for j in lst:
                if(i == j):
                    temp.append(i)
            result.append(temp)
            added_elements.append(i)
        
    return result

print(advanced_sort(["b", "a", "b", "a", "c"]))
            

