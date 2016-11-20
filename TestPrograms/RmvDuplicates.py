inpwords = raw_input()

wordslist = [word for word in inpwords.split(" ")]

print word
print wordslist

print " ".join(sorted(set(wordslist)))