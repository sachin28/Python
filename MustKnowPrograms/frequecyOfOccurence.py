file = open('names.txt')
line = file.readline()
count_list = {}
max_word = None
max_count = 0

while line:

    line = line.strip()
    if line in count_list:
        count_list[line] += 1
    else:
        count_list[line] = 1

    if count_list[line] > max_count:
        max_count = count_list[line]
        max_word = line

    line = file.readline()

print count_list

print max_word
print max_count

print max(count_list.values())
