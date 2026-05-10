def coin_count(coin_list, amount):
    result = float("inf")

    def conver_to_descending(list):
        for i in range(len(list)):
            for j in range(0, len(list) - i - 1):
                if list[j] < list[j + 1]:
                    list[j],list[j+1] = list[j+1],list[j]
        return list

    def get_total_coins(list):
        target_amount = amount
        total_coin = 0
        while target_amount > 0:
            coin_receive = False
            for coin in list:
                if coin <= target_amount:
                    target_amount -= coin
                    total_coin += 1
                    coin_receive = True
                    break
            
            if coin_receive == False:
                return -1
        return total_coin
    
    descending_list = conver_to_descending(coin_list)
    
    for i in range(len(descending_list)):
        current_result = get_total_coins(descending_list[i:])

        if(current_result > 0 and current_result < result):
            result = current_result
        
    return -1 if result == float("inf") else result


# print(coin_count([2,5,10,1], 27))
# print(coin_count([1,2,5], 11))
# print(coin_count([2], 3))
# print(coin_count([2,5,10], 27))
# print(coin_count([1,3,4], 6))