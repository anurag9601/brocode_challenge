def interview(input_lst, taken_time):
    attempt_questions = 0
    total_time = 0
    for i in input_lst:
        attempt_questions += 1
        total_time += i
    total_time += 20 #Interview buffer time
    print(total_time)
    print(attempt_questions)
    if(attempt_questions == 8 and total_time <= 120 and taken_time <= 120):
        return "qualified"
    else:
        return "disqualified"

# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
# print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
# print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))
# print(interview([5, 5, 10, 10, 15, 15, 20], 120))
# print(interview([5, 5, 10, 10, 15, 15, 20, 20], 130))
