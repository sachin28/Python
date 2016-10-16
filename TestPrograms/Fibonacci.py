
def fib_iterative(n):


    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

n = int(raw_input()) - 1
print  fib_iterative(n)


