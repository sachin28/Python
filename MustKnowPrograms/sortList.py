data_list = [-9, 2, 87, 4, 0, -28, -9]

sorted_list = []



while data_list:

    min = data_list[0]
    for number in data_list:
        if number < min:
            min = number
    sorted_list.append(min)
    data_list.remove(min)


print sorted_list