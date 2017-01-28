import re

given_string = '''Sachin is 24 years old and his mom Shashi is 49 years old'''

ages = re.findall(r'\d{1,2}', given_string)

name = re.findall(r'[A-Z][a-z]*', given_string)

print ages
print name

dic = {}
i = 0

for eachname in name:
    dic[eachname] = ages[i]
    i += 1

print dic
