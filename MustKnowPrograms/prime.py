def prime():
    'checking prime for 9 numbers'
    for i in range(10):
        if i:
            number = abs(int(raw_input("\r\nInsert any number to check its primarility: ")))

            if number == 0 or number == 1:
                print "not a prime"

            else:
                flag = 0
                for x in range(2, (number / 2) + 1):
                    if number % x == 0:
                        flag = 1
                        break

                if flag == 1:
                    print "not a prime"
                else:
                    print "is a prime"


prime()
