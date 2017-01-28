odd = []
count = 0
for n in range(1, 100):
    if n % 2 == 1:
        # print str(n)+" is an odd number"
        odd.append(n)
        count = count + 1
print odd
print 'number of odds: {}'.format(count)
