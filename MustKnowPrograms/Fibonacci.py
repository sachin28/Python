val = int(raw_input("Enter the number to get fib: "))


def fibo(val):
    if val == 0 or val == 1:
        return val

    return fibo(val - 1) + fibo(val - 2)


print 'Requested Fibo is {}'.format(fibo(val))
