# fibonacci series

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)

print(fibonacci(10))

def fibonacci_manual(n):
    a = 0
    b = 1
    c = 1

    if n <= 1:
        return n

    for _ in range(n):
        c = a + b
        b = a
        a = c
    
    return c

print(fibonacci_manual(10))
