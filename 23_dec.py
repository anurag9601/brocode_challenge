def is_happy(n):
    str_n = str(n)

    while(len(str_n) != 1):
        current_sum = 0
        for i in str_n:
            i = int(i)
            current_sum += i**2
        str_n = str(current_sum)

    if(int(str_n) == 1):
        return True
    else:
        return False

def is_happy_using_recur(n):
    str_n = str(n)

    len_str_n = len(str_n)

    if(len_str_n == 1 and n == 1):
        return True
    elif(len_str_n == 1 and n > 1):
        return False
        
    current_sum = 0

    for i in str_n:
        i = int(i)
        current_sum += i**2
    return is_happy_using_recur(int(current_sum))
        

# print(is_happy(67))
# print(is_happy(139))
# print(is_happy_using_recur(139))
# print(is_happy_using_recur(67))
