def anagram(word1, word2):
    char_dict = {}

    for char in word1:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    for char in word2:
        count = char_dict.get(char)

        if not count:
            return None
        elif count == 1:
            char_dict.pop(char)
        else:
            char_dict[char] -= 1

    return True if len(char_dict) == 0 else False


result = anagram('silent', 'listen1')
assert result == False

'''
string = 'aabccdb'
str =  'abcacbd'



l1 =  list(string)
l2 = list(str)

l1.sort()
l2.sort()

if l1== l2:
    print 'anagram'
'''
