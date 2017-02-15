l = [1, 2, 3, 4, 5]  # return [2,3,4,5,6]

# way 1
result = []
for element in l:
    result.append(element + 1)

print result

# way 2
for index in range(0, len(l)):
    l[index] += 1

print l

print [x + 1 for x in l]

print map(lambda x: x + 1, l)
