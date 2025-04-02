def prime_fectors(n):
    result = []
    divisor = 2
    while(n != 1):
        while(n%divisor != 0):
            divisor += 1
        result.append(divisor)
        n = n // divisor
    return result

# print(prime_fectors(20))
# print(prime_fectors(100))
# print(prime_fectors(8912234))

def formula(sum_str):
    if sum_str == "":
        return None
    
    op = {
        "+": lambda x,y: x + y,
        "-": lambda x,y: x - y,
        "*": lambda x,y: x * y,
        "/": lambda x,y: x / y
    }
    split_sum_str = sum_str.split("=")
    result = int(split_sum_str[-1])
    sum_values = split_sum_str[0].split(" ")
    operator = sum_values[1]
    x = int(sum_values[0])
    y = int(sum_values[2])

    expression_sum = op[operator](x,y)

    return expression_sum == result

print(formula("6 * 4 = 24"))
print(formula("18 / 17 = 2"))
print(formula(""))


