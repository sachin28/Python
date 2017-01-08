integer = int(raw_input("input an integer: "))

list = [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17]

try:
    for number in list:
        diff = integer-number
        if diff in list:
            print '{} and {} makes the sum {}'.format(number,diff,integer)
            break

except:
    print 'not possible'