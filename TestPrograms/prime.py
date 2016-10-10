def prime():
    'checking prime for 9 numbers'
    for i in range (10):
        if i:
            number = int(raw_input("\r\nInsert any number to check its primarility: "))
            flag = 0
            for x in range(2,(number/2)+1):
                if number % x == 0:
                    flag = 1
                    break

            if flag == 1:
                print +number," not a prime"
            else:
                print +number, "is a prime"


prime()