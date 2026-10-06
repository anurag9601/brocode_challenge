def is_palindrome(s, alphabet = "abcdefghijklmnopqrstuvwxyz"):
    print("s", s)
    print("len s", len(s))
    if len(s) <= 1:
        if len(s) == 0:
            print("true")
            return True
        elif len(s) == 1 and s[0] not in alphabet:
            print("true")
            return True
        else:
            print("false")
            return False

    i = s[0].lower()
    j = s[-1].lower()

    if i in alphabet and j in alphabet:
        if i != j:
            print("false")
            return False
        else:
            is_palindrome(s[1:-1], alphabet)
    else:
        if i not in alphabet:
            s = s[1:]
        if j not in alphabet:
            s = s[:-1]
        is_palindrome(s, alphabet)

# print(is_palindrome("Go hang a salami, I'm a lasagna hog!"))
# print(is_palindrome("This phrase, surely, is not a palindrome!"))
print(is_palindrome("Eva, can I see bees in a cave?"))