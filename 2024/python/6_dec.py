#Problem 1
# Find the Highest Integer in the List Using Recursion
# Create a function that finds the highest integer in the list using recursion.

# Examples
# find_highest([-1, 3, 5, 6, 99, 12, 2]) ➞ 99

# find_highest([0, 12, 4, 87]) ➞ 87

# find_highest([8]) ➞ 8

#Solution
def find_highest(lst):
    max = float("-inf")
    if(len(lst) == 1):
        max = lst[0]
        return max
    else:
        max = find_highest(lst[1:])
        return max if (max > lst[0]) else lst[0]

#Problem 2
# Burglary Series (03): Is It Gone?
# Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!

# Given a dictionary of the stolen items and a string in lowercase representing the name of the pet (e.g. "rambo"), return:

# "Rambo is gone..." if the name is on the list.
# "Rambo is here!" if the name is not on the list.
# Note that the first letter of the name in the return statement is capitalized.

#Solution
def is_item_stolen(items):
    find_item = input("Enter the item name want to check: ")
    for item in items.keys():
        if(item == find_item):
            return f"{find_item} is gone..."
    return f"{find_item} is here!"

#Problem 3
# Finding Common Elements
# Create a function that takes two lists of numbers sorted in ascending order and returns a list of numbers which are common to both the input lists.

# Examples
# common_elements([-1, 3, 4, 6, 7, 9], [1, 3]) ➞ [3]

# common_elements([1, 3, 4, 6, 7, 9], [1, 2, 3, 4, 7, 10]) ➞ [1, 3, 4, 7]

# common_elements([1, 2, 2, 2, 3, 4, 5], [1, 2, 4, 5]) ➞ [1, 2, 4, 5]

# common_elements([1, 2, 3, 4, 5], [10, 12, 13, 15]) ➞ []

def common_elements(lst1, lst2):
    result = []
    for i in lst1:
        if(i in lst2 and i not in result):
            result.append(i)
    return result

#Problem 4
# Create a function that returns any of the items you can afford in the store with the money you have in your wallet. Sort the list in alphabetical order.

# Examples
# items_purchase({
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }, "$300") ➞ ["Bread", "Fertilizer", "Water"]

# items_purchase({
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
#   }, "$100") ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

# items_purchase({
#   "Phone": "$999",
#   "Speakers": "$300",
#   "Laptop": "$5,000",
#   "PC": "$1200"},
# "$1") ➞ "Nothing"

#Solution
def items_purchase(item_dict, wallet):
    purchase_item_lst = []

    wallet = wallet.replace("$", "")
    if("," in wallet):
        wallet.replace(",", "")

    remain_money = int(wallet)

    for key, value in item_dict.items():
        value = value.replace("$", "")
        if("," in value):
            value = value.replace(",", "")
        value = int(value)
        if(value < remain_money):
            purchase_item_lst.append(key)
            remain_money -= value

    purchase_item_length = len(purchase_item_lst)

    #Arranging list items in the alphabetical order using bubble soring 
    for i in range(purchase_item_length):
        for j in range(0, purchase_item_length-i-1):
            if(purchase_item_lst[j] > purchase_item_lst[j+1]):
                purchase_item_lst[j],purchase_item_lst[j+1] = purchase_item_lst[j+1],purchase_item_lst[j]

    return purchase_item_lst

print(items_purchase({
  "Water": "$1",
  "Bread": "$3",
  "TV": "$1,000",
  "Fertilizer": "$20"
}, "$300"))


    