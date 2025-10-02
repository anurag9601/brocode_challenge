# Smart City — Traffic Signal Scheduling (Hard)

# In a smart city, traffic signals switch between red and green. A green light allows cars to pass, but only a certain number of cars per cycle.

# Create a function that takes:
# number of cars waiting,
# cycle capacity (cars per green),
# number of cycles.
# Return how many cars remain after the cycles.

def traffic(present_cars, car_pass_limit, signal_green_count):
    for i in range(signal_green_count):
        present_cars -= car_pass_limit
        if present_cars < 0:
            return 0
    return present_cars

# print(traffic(50, 12, 3))
# print(traffic(20, 5, 2))
# print(traffic(5, 2, 2))
# print(traffic(3, 5, 1))
# print(traffic(0, 0, 0))

# Flight Boarding — Passenger Groups (Hard)
# At an airport, passengers board in groups. Each group must be seated together, and each row has 6 seats.
# Create a function that assigns groups to rows.

def boarding(passengers_list):
    seat_limit = 6
    seating_arragements = []

    curr_row = []
    seated_pass = 0
    for passenger in passengers_list:
        curr_pass_count = seated_pass + passenger
        if curr_pass_count > seat_limit:
            seating_arragements.append(curr_row)
            seated_pass = 0
            curr_row = []

            seated_pass += passenger
            curr_row.append(passenger)
        else:
            seated_pass += passenger
            curr_row.append(passenger)
    if len(curr_row) > 0:
        seating_arragements.append(curr_row)
    return seating_arragements

# print(boarding([6, 2, 2, 2, 5]))
# print(boarding([2, 4, 3, 5]))