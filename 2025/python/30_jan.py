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


def dif_ciph(input_str):
    def custom_ord(char):
        if( not isinstance(char, str) or len(char) != 1):
            raise TypeError("not a string or an empty string")
    
        result = 0
        for i in range(len(char)):
            result = (result << 8) + (lambda c: c.encode("utf-8")[0])(char)

        return result
    
    prev = 0
    encoded_num = []

    for char in input_str:
        current = custom_ord(char)
        if(prev == 0):
            encoded_num.append(current)
            prev = current
        else:
            encoded_num.append(current - prev)
            prev = current

    return encoded_num

# print(dif_ciph("Hello"))
# print(dif_ciph("Sunshine"))