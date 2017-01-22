file = open('names.txt')
line = file.readline()
count_list = {}



while line:

    line = line.strip()
    if line in count_list:
        count_list[line] += 1
    else:
        count_list[line] = 1

    line = file.readline()



print count_list







