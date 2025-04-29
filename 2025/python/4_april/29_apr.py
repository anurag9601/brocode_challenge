def generate_noncosecutive(n):

    lst = ["0", "1"]

    if n == 1:
        return " ".join(lst)
    
    for i in range(2, n + 1):
        temp_l = []
        index = 0
        add = "0"
        while True:
            if add == "1" and lst[index][0] == "1":
                break
            elif index == len(lst):
                add = "1"
                index = 0
            else:
                temp_l.append(add + lst[index])
                index += 1
        lst = temp_l
    
    return " ".join(lst)

# print(generate_noncosecutive(1))
# print(generate_noncosecutive(2))
# print(generate_noncosecutive(3))
# print(generate_noncosecutive(4))

def maximum_seating(seats):
    seating_area = 0

    index = 0

    while index < len(seats):
        if index == 0 and seats[index] == 0 and seats[index + 1] == 0 and seats[index + 2] == 0:
            seating_area += 1
            index += 3
        elif index == len(seats) - 1 and seats[index] == 0 and seats[index - 1] == 0 and seats[index - 2] == 0:
            seating_area += 1
            index += 3
        elif index >= len(seats) - 3 and seats[index] == 0 and seats[index + 1] == 0 and seats[index + 2] == 0:
            seating_area += 1
            index += 3
        else:
            index += 1
        
    return seating_area

# print(maximum_seating([0, 0, 0, 1, 0, 0, 1, 0, 0, 0]))
# print(maximum_seating([0, 0, 0, 0]))
# print(maximum_seating([1, 0, 0, 0, 0, 1]))
# print(maximum_seating([1, 1, 1, 1, 1]))
# print(maximum_seating([0, 0, 0, 1, 0, 1, 0, 0, 0]))
# print(maximum_seating([0, 0, 0, 1, 0, 0, 0, 0]))

