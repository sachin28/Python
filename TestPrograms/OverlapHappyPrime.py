primelist = []
with open('primelist.txt') as prime:
    line = prime.readline()
    while line:
        primelist.append(int(line))

        line = prime.readline()

happylist = []
with open('happylist.txt') as happy:
    line = happy.readline()
    while line:
        happylist.append(int(line))

        line = happy.readline()

intersectionlist = []
for intlst in primelist:
    if intlst in happylist:
        intersectionlist.append(intlst)

print(intersectionlist)