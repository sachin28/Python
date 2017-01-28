value = []
items = [x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)  # converts binary to decimal

    if intp % 5 == 0:
        value.append(p)
    else:
        continue

print ','.join(value)
