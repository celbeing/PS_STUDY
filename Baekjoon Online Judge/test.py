import sys
input = sys.stdin.readline

n, m = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, m):
    field[0][i] += field[0][i - 1]
for i in range(1, n):
    field[i][0] += field[i - 1][0]
    for j in range(1, m):
        field[i][j] += max(field[i - 1][j], field[i][j - 1])

print(field[-1][-1])