elements = [1, 2, 3]

for value in elements:
    print value
print ""


for value in elements[::-1]:
    print value
print ""

for value in enumerate(elements):
    print value
print ""

for value in range(0, 6, 1):
    print value
print ""

for value in enumerate(elements):
    a = value[0]
    b = value[1]
    print a
    print b
print ""

for value in enumerate(elements):
     a, b = value

     print a
     print b
     


