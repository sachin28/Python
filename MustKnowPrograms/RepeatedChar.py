'''
find first repeacted char in string
'''


def first_repeated_char(str):
    for count, char in enumerate(str):
        if char in str[:count] or char in str[count + 1:]:
            print char
            break


if __name__ == '__main__':
    str = 'abcfghjkja'
    first_repeated_char(str)
