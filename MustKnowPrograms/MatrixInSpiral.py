matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

top = 0
bottom = len(matrix)
left = 0
right = len(matrix[0])
d = 0

while (top <= bottom and left <= right):
    if d == 0:
        for i in range(left, right):
            print matrix[top][i]
        top += 1
        d = 1

    if d == 1:
        for i in range(top, bottom):
            print matrix[i][right - 1]
        right -= 1
        d = 2

    if d == 2:
        for i in range(right - 1, left - 1, -1):
            print matrix[bottom - 1][i]
        bottom -= 1
        d = 3

    if d == 3:
        for i in range(bottom - 1, top - 1, -1):
            print matrix[i][left]
        left += 1
        d = 0
