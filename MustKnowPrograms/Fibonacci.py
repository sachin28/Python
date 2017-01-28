val = int(raw_input("Enter the number to get fib: "))


def fibo(val):
    if val == 0:
        return 0
    elif val == 1 or val == 2:
        return 1

    return fibo(val - 1) + fibo(val - 2)


print 'Requested Fibo is {}'.format(fibo(val))
