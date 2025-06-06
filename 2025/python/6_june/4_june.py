def is_palidrome(s, plain_s = "",left = 0):
    ignore_char = [" ", ",", "'", "?", "!"]
    
    if left == len(s) - 1:
        return plain_s == plain_s[::-1]
    else:
        if s[left] not in ignore_char:
            plain_s += s[left].lower()
        left += 1
    return is_palidrome(s, plain_s,left)

# print(is_palidrome("Go hang a salami, I'm a lasagna hog!"))

