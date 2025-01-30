def atbash(input_str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    lst_input_str = [*input_str]
    for i in range(len(lst_input_str)):
        isUpper = False
        if(lst_input_str[i].lower() in alphabet):
            index = alphabet.index(lst_input_str[i].lower())
            if(alphabet[index] != lst_input_str[i]):
                isUpper = True
            if(isUpper == True):
                lst_input_str[i] = alphabet[(len(alphabet) - 1) - index].upper()
            else:
                lst_input_str[i] = alphabet[(len(alphabet) - 1) - index]
    return "".join(lst_input_str)
    
# print(atbash("apple"))
# print(atbash("Christmas is the 25th of December"))
