def fib(n):
    if n <= 0:
        return
    a, b = 1, 0
    while n > 0:
        a, b = a + b, a
        n -= 1
    return b