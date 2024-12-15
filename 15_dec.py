def find_missing_number(lst):
    min_num = float("inf")
    max_num = float("-inf")

    for n in lst:
        if(n > max_num):
            max_num = n
        if(n < min_num):
            min_num = n

    for num in range(min_num, max_num + 1):
        if(num not in lst):
            return num

# print(find_missing_number([1, 2, 3, 4, 5, 7]))
# print(find_missing_number([1, 2, 3, 4, 6]))

def validate_parantheses(input_str):
    temp_dic = {}

    if(input_str == ""):
        return True

    for i in input_str:
        count = 0
        for j in input_str:
            if(i == j):
                count = count + 1
        temp_dic[i] = count

    find_match = ""

    for keyi in temp_dic.keys():
        have_match = False

        if(keyi == "("):
            find_match = ")"
        if(keyi == "{"):
            find_match = "}"
        if(keyi == "["):
            find_match = "]"
        for keyj in temp_dic.keys():
            if(find_match == keyj):
                if(temp_dic[keyj] == temp_dic[keyi]):
                    have_match = True
        if(have_match == False):
            return False
    return True
            
# print(validate_parantheses("({[]})"))
# print(validate_parantheses("((()))"))
# print(validate_parantheses("(]"))
# print(validate_parantheses("({[]})"))
# print(validate_parantheses(""))

# Find Kth Largest Element in an Array

def find_largest_element(lst,k):
    for i in range(len(lst)):
        max_num_i = i
        for j in range(i, len(lst)):
            if(lst[max_num_i] < lst[j]):
                max_num_i = j
        lst[max_num_i],lst[i] = lst[i],lst[max_num_i]
    return lst[k-1]

# print(find_largest_element([3,2,1,5,6,4],2))
# print(find_largest_element([3, 2, 1, 5, 6, 4],1))
# print(find_largest_element([3, 2, 1, 5, 6, 4],6))




