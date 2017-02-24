def frequency(filename):
    wordcount = {}
    file = open(filename, 'r')
    maxword = None
    maxcount = 0

    for line in file:

        word_list = line.replace(',', '').replace('.', '').lower().split()

        for word in word_list:

            if word in wordcount:
                wordcount[word] += 1
            else:
                wordcount[word] = 1

            if wordcount[word] > maxcount:
                maxcount = wordcount[word]
                maxword = word

    print '{:20}{:4}'.format('word', 'frequency')
    print '-' * 30
    for word, frequency in wordcount.iteritems():
        print '{:20}{:4}'.format(word, frequency)
    print 'maximum word is "{}" with "{}" repetitions'.format(maxword, maxcount)
    
    file.close()


if __name__ == "__main__":
    frequency('test.txt')


'''
file = open('names.txt')
line = file.readline()
count_list = {}
max_word = None
max_count = 0

while line:

    line = line.strip()
    if line in count_list:
        count_list[line] += 1
    else:
        count_list[line] = 1

    if count_list[line] > max_count:
        max_count = count_list[line]
        max_word = line

    line = file.readline()

print count_list

print max_word
print max_count

print max(count_list.values())
'''
