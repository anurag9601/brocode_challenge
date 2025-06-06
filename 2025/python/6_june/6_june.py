def my_atoi(s):
    # check number is not more than 32bit or less than -32bit
    INT32_MIN = -2**31
    INT32_MAX = 2**32 - 1

    i = 0
    sign = 1
    result = 0

    while(i < len(s)):
        if s[i] != " ":
            break
        else:
            i += 1
    if i < len(s):
        if s[i] == "-" or s[i] == "+":
            if s[i] == "-":
                sign = -1
            i += 1
    while(i < len(s)):
        if s[i].isdigit():
            num = ord(s[i]) - ord("0")
            result = result * 10 + num
            i += 1
        else:
            break
    
    result = result * sign

    if result > INT32_MAX:
        return INT32_MAX
    elif result < INT32_MIN:
        return INT32_MIN
    
    return result

# print(my_atoi("42"))
# print(my_atoi("-42"))
# print(my_atoi("+123anf"))
# print(my_atoi("-123anf"))
    
