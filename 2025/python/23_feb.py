def longest_valid_parantheses(input_str):
    longest_paran = ""
    prev = ""

    for char in input_str:
        if len(longest_paran) == 0 and char == "(":
            longest_paran += "("
        elif char == "(" and len(longest_paran) > 0:
            if longest_paran[-1] == ")":
                longest_paran += char
            else:
                if len(longest_paran) > len(prev):
                    prev = longest_paran
                longest_paran = ""
        elif char == ")" and len(longest_paran) > 0:
            if longest_paran[-1] == "(":
                longest_paran += char
            else:
                if len(longest_paran) > len(prev):
                    prev = longest_paran
                longest_paran = ""

    return len(longest_paran) if len(longest_paran) > len(prev) else len(prev)

print(longest_valid_parantheses("((()"))
print(longest_valid_parantheses(")()())"))
print(longest_valid_parantheses("())()"))
