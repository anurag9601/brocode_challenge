#find the longest palindrome in the given string

def get_longest_palindrome(input_str):
    longest_palin = ""
    length_long_palin = 0

    if(len(input_str) == 1):
        return input_str
    else:
        for i in range(len(input_str)):
            temp = ""
            reverse_temp = ""
            for j in range(i, len(input_str)):
                temp += input_str[j]
                reverse_temp = temp[::-1]
                if(temp == reverse_temp):
                    if(length_long_palin < len(temp)):
                        longest_palin = temp
                        length_long_palin = len(temp)
        return longest_palin

# print(get_longest_palindrome("abcba12321"))
# print(get_longest_palindrome("forgeeksskeegfor"))
# print(get_longest_palindrome("aaaa"))
# print(get_longest_palindrome("a"))
# print(get_longest_palindrome("ac"))
