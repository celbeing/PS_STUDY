#11780: 플로이드 2
import sys
input = sys.stdin.readline
inf = 1e9
n = int(input())
m = int(input())
bus = [[inf] * (n+1) for _ in range(n+1)]
path = [[[] for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    if bus[a][b] > c:
        bus[a][b] = c
for k in range(1, n+1):
    for i in range(1, n+1):
        bus[i][i] = 0
        for j in range(1, n+1):
            t = bus[i][k] + bus[k][j]
            if bus[i][j] > t:
                bus[i][j] = t
                path[i][j] = path[i][k]+[k]+path[k][j]

for i in range(1, n+1):
    for j in range(1, n+1):
        if bus[i][j] == inf:
            bus[i][j] = 0

for i in range(1, n+1):
    print(*bus[i][1:])
for i in range(1, n+1):
    for j in range(1, n+1):
        if bus[i][j] > 0:
            print(len(path[i][j])+2, *[i]+path[i][j]+[j])
        else:
            print(0)