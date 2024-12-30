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