def fibonacci(start=(0, 1), stop=FIB_STOP):
    a, b = start
    while stop:
        yield a
        a, b = b, a + b
        stop -= 1
