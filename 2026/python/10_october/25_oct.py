def guess_score(code, guess):
    already_used_code = ""
    black_score = 0
    white_score = 0

    for i in range(len(code)):
        if guess[i] in already_used_code:
            continue
        elif code[i] == guess[i]:
            black_score = black_score + 1
            already_used_code = already_used_code + guess[i]
        elif code[i] in guess:
            white_score = white_score + 1
            already_used_code = already_used_code 

    return { "black": black_score, "white": white_score }

# print(guess_score("1423", "5678"))
# print(guess_score("1423", "2222"))
# print(guess_score("1423", "1234"))
# print(guess_score("1423", "2211"))

