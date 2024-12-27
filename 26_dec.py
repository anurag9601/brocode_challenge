def suffle_count(n):
    working_lst = [x for x in range(1,n+1)]
    first_half = working_lst[:len(working_lst)//2]
    second_half = working_lst[len(working_lst)//2:]
    suffle_count = 1
    length_count = 0
    suffle_complete = False

    while(suffle_complete == False):
        for i in range(len(working_lst)):
            if(i%2 != 0):
                first_half.insert(i, second_half[length_count])
                length_count += 1
        if(first_half == working_lst):
            suffle_complete = True
        else:
            second_half = first_half[len(first_half)//2:]
            first_half = first_half[:len(first_half)//2]
            suffle_count += 1
            length_count = 0
    return suffle_count

# print(suffle_count(8))
# print(suffle_count(14))
# print(suffle_count(52))


def num_of_days(amount, savings, current):
    week_start_value = current
    current_savings = savings
    no_of_days = 0

    while(current_savings < amount):
        for i in range(7):
            if(current_savings >= amount):
                break
            if(i == 0):
                current_savings += week_start_value
                no_of_days += 1
            else:
                current_savings += (week_start_value + i)
                no_of_days += 1
        week_start_value += 1
    return no_of_days

# print(num_of_days(500, 300, 50))
# print(num_of_days(2050, 1200, 10))
# print(num_of_days(10000, 2500, 50))
    
    
