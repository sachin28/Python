counter_dict = {}
f = open('names.txt')
line = f.readline()
while line:
    line = line.strip()
    if line in counter_dict:
        counter_dict[line] += 1

    else:
        counter_dict[line] = 1

    line = f.readline()

print (counter_dict)
