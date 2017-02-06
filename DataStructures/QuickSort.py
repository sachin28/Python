def quicksort(table, start, end):
    if start == end:
        return table

    i = start
    j = end
    pivot = (start + end) // 2

    while (i <= j):

        while (table[i] < table[pivot]):
            i += 1

        while (table[pivot] < table[j]):
            j -= 1

        if (i <= j):
            table[i], table[j] = table[j], table[i]
            i += 1
            j -= 1

    if j > start:
        quicksort(table, start, j)
    if i < end:
        quicksort(table, i, end)

    return table


if __name__ == '__main__':
    table = [10, 3, 5, 6, 15, 9, 1, 4, 2, 10, 99, 0]

    quicksort(table, 0, len(table) - 1)
    print table
