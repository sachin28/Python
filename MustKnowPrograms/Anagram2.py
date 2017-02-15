from collections import defaultdict


def anagram(str1, str2):
    d = defaultdict(int)

    for char in str1:
        d[char] += 1

    for char in str2:

        if d[char] == None:
            return None

        if d[char] == 1:
            d.pop(char)

        else:
            d[char] -= 1

    if len(d) == 0:
        print "anagram"


anagram("12", "21")
