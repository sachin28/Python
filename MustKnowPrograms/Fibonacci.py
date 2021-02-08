val = int(raw_input("Enter the number to get fib: "))


def fibo(val):
    if val == 1 or val == 2:
        return val

    return fibo(val - 1) + fibo(val - 2)


print 'Requested Fibo is {}'.format(fibo(val))
