import re

# input = raw_input()

input = '.172..16.52.207,172.16.52.117'

list = re.split(r'[\,\.]', input)

for l in list:
    if l != '':
        print l
