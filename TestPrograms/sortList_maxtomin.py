unsorted_list = [2,3,5,-1,8,2,99]
sorted_list = []


while unsorted_list:
    max = unsorted_list[0]
    for numbers in  unsorted_list:
        if numbers > max:
            max = numbers
    

    sorted_list.append(max)
    unsorted_list.remove(max)

#print unsorted_list
print sorted_list

