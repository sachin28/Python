def char_count(string):
    prev_char = None
    total_count = 0
    str_len = len(string)
    count = 0
    result = ""

    for char in string:

        total_count += 1

        if prev_char == None:
            prev_char = char
            count = 1

        elif prev_char == char:
            count += 1

        else:
            result = "{}{}{}".format(result, prev_char, count)
            prev_char = char
            count = 1

        if str_len == total_count:
            result = "{}{}{}".format(result, prev_char, count)

    return result


if __name__ == "__main__":
    string = "aaabcclllooppp"
    print char_count(string)
    
    # expected a3b1c2l3o2p3
