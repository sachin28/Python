from collections import defaultdict

file = open('vm', 'rb')
vm_dict = defaultdict(list)

for line in file:
    vm, operations = line.split(" ")

    # if vm in vm_dict:
    vm_dict[vm].append(operations)
    # else:
    #   vm_dict[vm] = [operations]

print vm_dict;

for key, value in vm_dict.iteritems():
    print "{}   {}    {}".format(
        key, len(value), " ".join(value)
    )

file.close()
