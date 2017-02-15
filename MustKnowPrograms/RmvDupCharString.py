string = 'aabccdb'

unique = ''

for char in string:
    if char not in unique:
        unique = unique + char
print unique
