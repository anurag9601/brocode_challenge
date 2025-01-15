def get_prices(input_lst):
    result = []
    for prices in input_lst:
        split_product_price = prices.split("($")
        result.append(float(split_product_price[1][:-1]))
    return result

# print(get_prices(["salad ($4.99)"]))
# print(get_prices([
#   "artichokes ($1.99)",
#   "rotiserrie chicken ($5.99)",
#   "gum ($0.75)"
# ]))
# print(get_prices([
#   "ice cream ($5.99)",
#   "banana ($0.20)",
#   "sandwich ($8.50)",
#   "soup ($1.99)"
# ]))