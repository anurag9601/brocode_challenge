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

def num_split(n):
    result = []
    is_nagative = False

    if(n < 0):
        is_nagative = True
        n = n * -1

    count = 0

    while(n != 0):
        temp = str(n%10)
        n = n//10
        for i in range(count):
            temp += "0"
        if(is_nagative == True):
            temp = int(temp) * -1
            result.insert(0, temp)
        else:
            temp = int(temp)
            result.insert(0, temp)
        count += 1
    return result

# print(num_split(-434))
# print(num_split(100))
# print(num_split(39))
# print(num_split(1234))

        

