def str_to_char_count(s):
    result = ""
    prev_char = s[0]
    count = 1

    for i in range(1,len(s)):
        if s[i] != prev_char:
            result += f"{prev_char}{count}"
            prev_char = s[i]
            count = 1
        else:
            prev_char = s[i]
            count += 1
    result += f"{prev_char}{count}"
    return result

print(str_to_char_count("anuraag"))
        