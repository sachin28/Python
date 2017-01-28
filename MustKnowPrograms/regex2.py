import re

m = int(raw_input())
count = 1
while count:
    input = raw_input()
    print bool(re.match(r'^[+-.]?[0-9]*\.[0-9]+$', input))
    count += 1

# check for integer
# for this input

'''
4
4.0O0
-1.00
+4.54
SomeRandomStuff
'''
