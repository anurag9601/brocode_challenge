# Coffee Machine — Cup Filling 
#  You’re building a smart coffee machine. It can brew cups of coffee, but it has a water tank with limited capacity.

# Each small cup uses 200 ml of water, and each large cup uses 350 ml.

# Create a function that takes the tank capacity (in ml) and the number of cups brewed, then returns how many large cups and small cups could be filled before the machine runs out of water.

def coffee(total_water, coffee_list):
    small_coffee_req = 200
    large_coffee_req = 350

    created_coffee = 0

    for coffee in coffee_list:
        if coffee == "small" and total_water >= small_coffee_req:
            total_water -= small_coffee_req
            created_coffee += 1
        elif coffee == "large" and total_water >= large_coffee_req:
            total_water -= large_coffee_req
            created_coffee += 1
        else:
            return created_coffee
    return created_coffee
        
# print(coffee(1000, ["small", "small", "large", "small"]))
# print(coffee(750, ["large", "large", "small"]))

# Elevator Weight Limit

# An elevator in a mall has a maximum weight capacity. Each person entering adds to the total load.

# Create a function that takes the elevator’s weight limit and a list of people’s weights, and returns the maximum number of people that can enter before exceeding the limit.

def elevator(weight_limit, people_weights):

    total_people_allow = 0
    loaded_weight = 0

    for weight in people_weights:
        if weight_limit <= loaded_weight + weight:
            continue
        elif weight_limit > loaded_weight + weight:
            loaded_weight += weight
            total_people_allow += 1
    return total_people_allow

# print(elevator(500, [80, 120, 150, 90, 60]))
# print(elevator(200, [100, 120, 90]))

