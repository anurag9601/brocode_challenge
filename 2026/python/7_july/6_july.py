def bank_transactions_total(transactions):
    process_transactions = []
    total_balance = 0

    for transaction in transactions:
        tran_no = transaction[0]
        amount = transaction[1]

        if tran_no not in process_transactions:
            if amount > 0:
                total_balance = total_balance + amount
            elif amount < 0:
                total_balance = total_balance - (amount * -1)
            process_transactions.append(tran_no)
    return total_balance

# print(bank_transactions_total([
#     ("T101", 500),
#     ("T102", -100),
#     ("T103", 250),
#     ("T101", 500),
#     ("T104", -50)
# ]))

# print(bank_transactions_total([
# ("A",100),
# ("B",-30),
# ("A",100),
# ("C",-20)
# ]))

def e_commerce_inventory(inventory, orders):
    failed_orders = []

    for order in orders:
        or_no = order[0]
        item = order[1]
        quantity = order[2]

        if inventory[item] >= quantity:
            inventory[item] = inventory[item] - quantity
        else:
            failed_orders.append(or_no)
    
    return f"Inventory {inventory} \nFailed Orders {failed_orders}"

# print(e_commerce_inventory({
# "Laptop":5,
# "Mouse":10,
# "Keyboard":3
# }, [
# ("O1","Laptop",2),
# ("O2","Mouse",5),
# ("O3","Laptop",4),
# ("O4","Keyboard",3),
# ("O5","Keyboard",1)
# ]))

# print(e_commerce_inventory({
# "A":1
# }, [
# ("1","A",1),
# ("2","A",1)
# ]))
