def longest_palindrom(s):
    longest_pali = ""
    for i in range(len(s)):
        temp = ""
        for j in range(i, len(s)):
            temp += s[j]
            if(temp == temp[::-1]):
                if(len(temp) > len(longest_pali)):
                    longest_pali = temp
    return longest_pali

# print(longest_palindrom("babad"))
# print(longest_palindrom("cbbd"))
# print(longest_palindrom("a"))
