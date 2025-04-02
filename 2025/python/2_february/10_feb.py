#Check is price using recursion

def is_prime_recus(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return is_prime_recus(n, divisor - 1)

def truncatable(n):
    str_n = str(n)

    truncatable = False

    if "0" in str_n:
        return truncatable

    def is_prime(num, divisor = None):
        if num <= 1:
            return False
        for i in range(2, round(num ** 0.5) + 1):
            if( num % i == 0):
                return False
        return True

    for i in range(len(str_n)):
        is_prime_num = is_prime(int(str_n[i:]))
        if not is_prime_num:
            break
        elif is_prime_num and i == len(str_n) - 1:
            truncatable = "left"

    for i in range(len(str_n), 0, -1):
        is_prime_num = is_prime(int(str_n[0:i]))
        if not is_prime_num:
            break
        elif is_prime_num and i == 1:
            if truncatable == "left":
                truncatable = "both"
            else:
                truncatable = "right"

    return truncatable

# print(truncatable(1234))
# print(truncatable(9137))
# print(truncatable(5939))
# print(truncatable(317))
# print(truncatable(5))
# print(truncatable(139))
# print(truncatable(103))


