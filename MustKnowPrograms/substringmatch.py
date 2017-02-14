def substring(string, subs):
    start = 0
    end = 0

    while start < len(string):
        if string[start + end] != subs[end]:
            start += 1
            end = 0
            continue
        end += 1

        if len(subs) == end:
            return start
    return -1


print substring("sachinshukla", "shukla")
