import random

k = int(raw_input("enter the k value: ")) #for kth largest value
# unsorted_list = [2,3,5,-1,8,2,99]
unsorted_list = [int(1000*random.random()) for i in xrange(10000)]
sorted_list = []

"""
while unsorted_list:
    max = unsorted_list[0]
    for numbers in  unsorted_list:
        if numbers > max:
            max = numbers
    

    sorted_list.append(max)
    unsorted_list.remove(max)

print sorted_list

print sorted_list[k-1]   #for kth largest value

"""

def quick_sort(table, start, end):
    if start == end:
        return table

    i = start
    j = end
    pivot = (start + end) // 2

    while(i <= j):
        while(table[i] < table[pivot]):
            i += 1

        while(table[j] > table[pivot]):
            j -= 1

        if (i <= j):
            table[i], table[j] = table[j], table[i]
            i += 1
            j -= 1


    if j > start:
        quick_sort(table, start, j)
    if i < end:
        quick_sort(table, i, end)


    return table



quick_sort(unsorted_list, 0, len(unsorted_list) - 1)

print unsorted_list[k * -1]
