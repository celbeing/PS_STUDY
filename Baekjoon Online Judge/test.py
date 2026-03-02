import sys
input = sys.stdin.readline
def solution():
    n = 90030
    table = [[0] * 3001 for _ in range(3001)]
    count = [[0] * 3001 for _ in range(3001)]
    x, y = -1500, -1500
    for _ in range(n):
        if y > 1500:
            x += 1
            y = -1500
        table[x][y] += 1
        count[x][y] += 1
        y += 1

    for y in range(-1499, 1501):
        table[-1500][y] += count[-1500][y - 1]
        table[-1500][y] += table[-1499][y - 1]
        for x in range(-1499, 1500):
            table[x][y] += count[x][y - 1]
            table[x][y] += table[x + 1][y - 1] + table[x - 1][y - 1] - (0 if y == -1499 else table[x][y - 2])
        table[1500][y] += count[1500][y - 1]
        table[1500][y] += table[1499][y - 1]

    x, y = -1500, -1500
    for _ in range(90030):
        if y > 1500:
            x += 1
            y = -1500
        print(table[x][y])

        y += 1
solution()