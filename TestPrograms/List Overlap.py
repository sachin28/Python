a = [3,6,8,13,89,24,55]
b = [1,1,2,3,5,8,13,21,34,55,89]

list = []

for number in a:
    if number in b:
        list.append(number)
print list


