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