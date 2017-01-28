primelist = []
prime = open('primelist.txt')
line = prime.readline()
while line:
    primelist.append(int(line))

    line = prime.readline()

happylist = []
happy = open('happylist.txt')
line = happy.readline()
while line:
    happylist.append(int(line))

    line = happy.readline()

intersectionlist = []
for intlst in primelist:
    if intlst in happylist:
        intersectionlist.append(intlst)

print(intersectionlist)
