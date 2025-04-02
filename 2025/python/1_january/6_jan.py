
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

def word_of_decimal(input_str, sum = 0, base = 0):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    if(base == 0):
        for i in input_str:
            if(base < alphabet.index(i.lower()) + 1):
                base = alphabet.index(i.lower()) + 1
        base += 10
    
    if len(input_str) == 0:
        return sum 
    
    k = len(input_str) - 1
    sum = sum + (alphabet.index(input_str[0].lower()) + 10) * base ** k
    return word_of_decimal(input_str[1:], sum)
        
# print(word_of_decimal("Edabit"))
# print(word_of_decimal("Python"))
# print(word_of_decimal("ZERO"))

    