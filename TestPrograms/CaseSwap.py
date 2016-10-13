inpstr = raw_input("Enter string input: ")

revstr= []

for i in inpstr:
    if i.isupper():
        i = i.lower()
        revstr.append(i)
    else:
        i = i.upper()
        revstr.append(i)

revstr = "".join(revstr)

print revstr
