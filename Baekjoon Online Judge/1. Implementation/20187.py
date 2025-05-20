#20187: 종이접기
import sys
input = sys.stdin.readline
k = int(input())
fold = list(input().split())
h = int(input())

paper = [[-1]*(1<<k) for _ in range(1<<k)]
x,y = 0,0
vert = 1<<k
hori = 1<<k

for d in fold:
    if d == 'D':
        vert >>= 1
        x += vert
    elif d == 'U':
        vert >>= 1
    elif d == 'R':
        hori >>= 1
        y += hori
    else:
        hori >>= 1

unfold = [(2,3,0,1),(1,0,3,2)]
paper[x][y] = h
for i in range(1<<k):
    for j in range(1<<k):
        if i == x and j == y: continue
        t = h
        if abs(i-x) & 1:
            t = unfold[0][t]
        if abs(j-y) & 1:
            t = unfold[1][t]
        paper[i][j] = t
    print(*paper[i])