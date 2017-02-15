
counter_dict = {}
# f = open('names.txt', "rb")
# line = f.readline()
max_val = 0
max_char = ""
with open("names.txt") as infile:
    #    print infile
    for line in infile:
        line = line.strip()
        if line in counter_dict:
            counter_dict[line] += 1
        else:
            counter_dict[line] = 1

        if counter_dict[line] > max_val:
            max_val = counter_dict[line]
            max_char = line

            # line = f.readline()

print (counter_dict)
print "{}:{}".format(max_char, max_val)
print "{}".format(max(counter_dict.values()))
