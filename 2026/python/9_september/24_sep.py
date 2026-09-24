def is_match(s, p): # s contain's string and p contain's the patters on which we have to verify the string is valid or not.
    if not s:
        return "The string is empty."
    
    if not p:
        return "Please enter the pattern on the basis of you have to verify."

    if all(char not in p for char in ".*") and (len(s) != len(p)):
        return False

    expected_char = p[0]
    pattern = "strict" # we are handling three patters strict/continue/flaxible

    def calculate_next_char(i):
        last_i = i
        if i > len(p):
            last_i = len(p)

        p_last_char = p[len(p) - 1]
        p_second_last_char = p[len(p) - 2]
        if p_last_char == "*" and p_second_last_char != ".":
            expected_char = s[i]
            pattern = "continue"
        elif p_second_last_char == ".":
            pattern = "flaxible"



    for i in range(len(s) - 1):
        if expected_char != s[i] and expected_char != "." and pattern != "flaxible":
            return False
        
        if len(p) > 2:
            calculate_next_char(i)
        else:
            return True
    return True
        

# print(is_match("ab", "a."))
# print(is_match("aa", "a*"))
# print(is_match("aa", "a"))
# print(is_match("ab", ".*"))
    
