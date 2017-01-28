from random import randint

limit = raw_input("Hit a number upto which you want to chose a random integer: ")

if not limit.isdigit():
    print ("Enter an integer value")

else:

    limit = int(limit)

    count = 0

    while (count < limit):
        diceValue = randint(1, limit)

        print(diceValue)

        count = count + 1
