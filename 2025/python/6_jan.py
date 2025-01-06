# def only_5_and_3(n):
#     if(n == 0):
#         return True
#     elif(n < 0):
#         return False
#     else:
        
def title_to_number(input_str):
    alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    index = 0
    for i in range(len(input_str)):
        index_of_current = alphabets.index(input_str[i])
        if(i == len(input_str) - 1):
            return index + (index_of_current + 1)
        else:
            index += 26 - index_of_current
    
# print(title_to_number("AB"))
# print(title_to_number("C"))
# print(title_to_number("Z"))


    