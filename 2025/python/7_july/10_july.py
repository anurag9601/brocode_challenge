def hangman(string, input_list):
    result = ""
    for i in string:
        if i in input_list or i == " ":
            result += i
        else:
            result += "-"
    return result

# print(hangman("helicopter", ["o", "e", "s"]))
# print(hangman("tree", ["r", "t", "e"]))