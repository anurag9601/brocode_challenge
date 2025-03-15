def longestPalindrome(s):
    longest_pali = ""

    for i in range(len(s)):
        current_pali = ""
        for j in range(i, len(s)):
            current_pali += s[j]
            if current_pali == current_pali[::-1] and len(current_pali) > len(longest_pali):
                longest_pali = current_pali
                if len(s) - i < len(longest_pali):
                    return longest_pali
    return longest_pali

# print(longestPalindrome("forgeeksskeegfor"))
# print(longestPalindrome("Geeks"))
# print(longestPalindrome("abc"))