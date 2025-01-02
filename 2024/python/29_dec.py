#only list 2 or 3 letter length of the string
def parmutations(input_str):
    result = []
    for i in range(len(input_str)):
        temp_lst = [*input_str]
        temp_lst.remove(temp_lst[i])
        if(len(input_str) == 3):
            for j in range(2):
                if(j == 1):
                    temp_lst[0],temp_lst[1] = temp_lst[1],temp_lst[0]
                for k in range(len(input_str)):
                    temp_lst.insert(k, input_str[i])
                    if("".join(temp_lst) not in result):
                        result.append("".join(temp_lst))
                    temp_lst.remove(input_str[i])
        else:
            for k in range(len(input_str)):
                temp_lst.insert(k, input_str[i])
                if("".join(temp_lst) not in result):
                    result.append("".join(temp_lst))
                temp_lst.remove(input_str[i])
    return result
            

# print(parmutations("AB"))
# print(parmutations("NOT"))
# print(parmutations("RAM"))
# print(parmutations("YAW"))


