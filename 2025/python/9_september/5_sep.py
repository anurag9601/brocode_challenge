def find_closest_delivery_partner(partners, orders):
    assign_orders = []

    for i in orders:
        if len(partners) == 1 and len(orders) == 1:
            assign_orders.append(partners[0])
            return assign_orders
        else:
            difference = float('inf')
            partner = 0
            for j in partners:
                if abs(i - j) < difference:
                    difference = abs(i - j)
                    partner = j
            assign_orders.append(partner)
    return assign_orders

# print(find_closest_delivery_partner([1, 5, 9], [2, 6, 8]))
# print(find_closest_delivery_partner([0, 10], [5]))
# print(find_closest_delivery_partner([2, 6, 12], [10]))
# print(find_closest_delivery_partner([0, 50], [25, 49, 51]))
# print(find_closest_delivery_partner([7, 7, 7], [7, 8]))



        