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

def freed_prisoners(prison_data):
    my_position = prison_data[0]

    if my_position == 0:
        return 0
    
    is_flip = False
    free_prisoners_count = 1 # just because my prison is open I'm the first free prisoner.

    for i in range(1, len(prison_data)):
        prison_condition = prison_data[i] if not is_flip else 1 - prison_data[i]

        if prison_condition == 0:
            free_prisoners_count += 1
            is_flip = not is_flip
        else:
            continue
    
    return free_prisoners_count

# print(freed_prisoners([1, 1, 0, 0, 0, 1, 0]))
# print(freed_prisoners([1, 1, 1]))
# print(freed_prisoners([0, 0, 0]))
# print(freed_prisoners([0, 1, 1, 1]))

# solving this problem for 2nd time and this is my shortest solution.
def staircase(steps):
    start_i = 1
    end_i = steps + 1
    step = 1
    if steps < 0:
        steps = (steps * -1)
        start_i = steps
        end_i = 0
        step = -1

    for step in range(start_i, end_i, step):
        print("_" * (steps - step), end="")
        print("#" * (step))

# print(staircase(7))
# print(staircase(-8))
    
