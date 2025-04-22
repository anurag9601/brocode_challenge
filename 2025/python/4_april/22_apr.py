def compress(chars):
    if len(chars) == 1:
        return chars[0]
        
    result = ""
    
    char_c = 1
    for i in range(len(chars) - 1):
        if chars[i] != chars[i+1]:
            if char_c > 1:
                result += f"{chars[i]}{char_c}"
            else:
                result += chars[i]
            char_c = 1
        elif chars[i] == chars[i+1]:
            char_c += 1
    if char_c > 1:
        result += f"{chars[-1]}{char_c}"
    else:
        result += chars[-1]
    
    return result
    
# print(compress(["a", "a", "b", "b", "c", "c", "c"]))
# print(compress(["a", "b"]))
# print(compress(["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]))
# print(compress(["a", "a", "a", "b", "b", "a", "a"]))