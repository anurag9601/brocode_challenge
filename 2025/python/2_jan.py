#Just for fun (stone paper sizer in python)😉
import random 

def stone_paper_sizer():
    choices = ["sizer", "paper", "stone"]
    game_over = False
    while(game_over == False):
        user_input = input("Enter [s]for sizer [p]for paper [S]for stone and [q]for quit:- ")
        user_choice = ""
        if(user_input == "q"):
            game_over = True
            break
        if(user_input == "s"):
            user_choice = "sizer"
        elif(user_input == "S"):
            user_choice = "stone"
        elif(user_input == "p"):
            user_choice = "paper"
        else:
            print("Invalid input")

        computer_choice = choices[random.randint(0,2)]

        if(user_choice == computer_choice):
            print(f"You choose:- {user_choice} || Computer choose:- {computer_choice}")
            print(f"It's a draw!")

        elif(user_choice == "sizer" and computer_choice == "paper" or user_choice == "paper" and computer_choice == "stone" or user_choice == "stone" and computer_choice == "sizer"):
            print(f"You choose:- {user_choice} || Computer choose:- {computer_choice}")
            print("You won!")

        elif(computer_choice == "sizer" and user_choice == "paper" or computer_choice == "paper" and user_choice == "stone" or computer_choice == "stone" and user_choice == "sizer"):
            print(f"You choose:- {user_choice} || Computer choose:- {computer_choice}")
            print("Computer won!")

        play_again = input("Want to play again y/n? :- ")
        if(play_again == "n" or play_again == "N"):
            game_over = True
        elif(play_again != "y" and play_again != "Y"):
            print("Invalid input play again!")

# stone_paper_sizer()

#Using stack algorithm(FILO or LOFI)
def isValidParentheses(input_s):

    if(len(input_s) % 2 != 0):
        return False

    stack = []

    paris = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in input_s:
        if char in paris.values():
            stack.append(char)
        elif char in paris.keys():
            if not stack or stack[-1] != paris[char]:
                return False
            stack.pop()
        else:
            return False

    return len(stack) == 0

# print(isValidParentheses("([])"))
# print(isValidParentheses("(]"))
# print(isValidParentheses("()[]{}"))
# print(isValidParentheses("()"))

