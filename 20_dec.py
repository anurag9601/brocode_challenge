def can_see_stage(lst):
    for i in range(len(lst[0])):
        for j in range(len(lst)-1):
            if(lst[i][j] > lst[i][j+1]):
                return False
    return True

# print(can_see_stage([
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]))
# print(can_see_stage([
#   [1, 0, 0],
#   [1, 1, 1],
#   [2, 2, 2]
# ]))
# print(can_see_stage([
#   [0, 0, 0],
#   [1, 1, 1],
#   [2, 2, 2]
# ]))

def shift_setence(input_str):
    split_input_str = input_str.split(" ")
    current_first_letter = split_input_str[0][0]
    for i in range(1,len(split_input_str)+1):
        if(i == len(split_input_str)):
            i = 0
        split_word = [*split_input_str[i]]
        words_first_letter = split_word[0]
        split_word[0] = current_first_letter
        split_word = "".join(split_word)
        split_input_str[i] = split_word
        current_first_letter = words_first_letter
    return " ".join(split_input_str)
    

# print(shift_setence("create a function"))
# print(shift_setence("it should shift the sentence"))
# print(shift_setence("Awesome"))

