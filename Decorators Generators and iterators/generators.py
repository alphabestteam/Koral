def fib(num_input):
    a, b = 0, 1
    for _ in range(num_input):
        yield a
        a, b = b, a + b
