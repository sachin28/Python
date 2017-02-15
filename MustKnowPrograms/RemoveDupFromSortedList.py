list1 = [1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7, 8, 8, 9, 9, 10, 10]

list2 = []

for count, int in enumerate(list1[:len(list1) - 2]):
    if int != list1[count + 1]:
        list2.append(int)

if list1[len(list1) - 1] == list1[len(list1) - 2]:
    list2.append(list1[len(list1) - 2])

else:
    list2.append(list1[len(list1) - 2])
    list2.append(list1[len(list1) - 1])

print list2
