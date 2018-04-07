""""Ip= [ [2,3],[3,5] , [7, 8], [10, 11],[12,14] ]
Op= [ [2, 5], [7, 8], [ 10,14]]"""

input = [[2,3],[3,5],[7,8],[10,11],[12,14]]

start = input[0]

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
