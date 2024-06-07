#11404: 플로이드
import sys
input = sys.stdin.readline
inf = 1e9

n = int(input())
m = int(input())
bus = [[inf for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    if bus[a][b] > c:
        bus[a][b] = c

for k in range(1,n+1):
    bus[k][k] = 0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if bus[i][j] > bus[i][k] + bus[k][j]:
                bus[i][j] = bus[i][k] + bus[k][j]

for i in range(1,n+1):
    for j in range(1,n+1):
        if bus[i][j] == inf:
            bus[i][j] = 0

for i in range(1,n+1):
    print(*bus[i][1:])