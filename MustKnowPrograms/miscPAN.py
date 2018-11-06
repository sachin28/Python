"""[cat, act, mat, atm, rat]
[ [cat, act], [mat, atm], [rat]]"""

input = ['cat', 'act', 'mat', 'atm', 'rat']
dict_name = {}

for name in input:
    sorted_name = ''.join(sorted(name))
    if not sorted_name in dict_name:
        dict_name[sorted_name] = [name]
    else:
        dict_name[sorted_name].append(name)
print dict_name.values()


"""[1, 2, 3, 5, 6, 7, 8, 9]  // 8"""
input = [1, 2, 3, 5, 5, 6, 7, 8, 9]
set_input = list(set(input))
target = 8
l = []
a = set()
for val in set_input:
    diff = (target - val)
    if val in a:
        l.append([diff, val])
    else:
        a.add(diff)
print l



"""Ip= [ [2,3],[3,5] , [7, 8], [10, 11],[12,14] ]
Op= [ [2, 5], [7, 8], [ 10,14]]"""

input = [[2,3],[3,5],[7,8],[10,11],[12,14]]


result = []

for curr_pair in input:

    if not result:
        result.append(curr_pair)
    else:
        last_pair = result[-1]
        if any([
            last_pair[1] - curr_pair[0] == 0,
            last_pair[1] - curr_pair[0] == -1
        ]):
            result[-1] = [last_pair[0], curr_pair[1]]
        else:
            result.append(curr_pair)
