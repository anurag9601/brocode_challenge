#Handling regular expressions
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

def freed_prisoners(lst):
    free_pres = 0

    if(lst[0] == 0):
        return 0
    else:
        for i in range(len(lst)):
            if(lst[i] == 1):
                for j in range(len(lst)):
                    if(lst[j] == 0):
                        lst[j] = 1
                    else:
                        lst[j] = 0
                free_pres += 1
                print(lst)
            
        return free_pres

# John is playing a dice game. The rules are as follows.

# Roll two dice.
# Add the numbers on the dice together.
# Add the total to your overall score.
# Repeat this for three rounds.
# But if you roll DOUBLES, your score is instantly wiped to 0 and your game ends immediately!

# Create a function that takes in a list of tuples as input, and return John's score after his game has ended.

#Solution
def dice_game(lst):
    final_score = 0

    for i in lst:
        if(i[0] == i[1]):
            return 0
        else:
            final_score += (i[0] + i[1])
    return final_score

#Problem
# Create a function that takes a dictionary of objects like { "name": "John", "notes": [3, 5, 4] } and returns a dictionary of objects like { "name": "John", "top_note": 5 }.

#Solution
def top_note(obj):
    for key,values in obj.items():
        max = float("-inf")
        if(key == "notes"):
            for j in values:
                if(j > max):
                    max = j
            del obj[key]
            break
    obj["top_note"] = max
    return obj

