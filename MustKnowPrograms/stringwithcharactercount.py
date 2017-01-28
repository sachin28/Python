givenString = 'aaabbccccddccffddd'

# expected o/p 'a3 b2....'

str_count = len(givenString)
count = None
prev_char = None

total_count = 0
for char in givenString:
    total_count += 1
    if prev_char is None:
        prev_char = char
        count = 1
    elif char == prev_char:
        count = count + 1
    else:
        print prev_char + str(count),
        prev_char = char
        count = 1

    if total_count == str_count:
        print prev_char + str(count)
