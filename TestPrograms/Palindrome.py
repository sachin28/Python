word = raw_input("Enter a word: ")
revword = word[::-1]

if word == revword:
    print ("It is a palindrome")

elif word != revword:
    print ("It is not a palindrome")

else:
    print ("Something went wrong")


