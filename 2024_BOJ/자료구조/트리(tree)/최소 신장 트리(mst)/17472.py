#17472: 다리 만들기 2
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
ground = [list(map(int,input().split())) for _ in range(N)]
island = [[0 for _ in range(M)] for _ in range(N)]
d = [(0,1),(1,0),(0,-1),(-1,0)]
bfs = deque()

number = 0
for k in range(N*M):
    n = k // M
    m = k % M
    if ground[n][m] == 1 and island[n][m] == 0:
        bfs.append((n,m))
        number += 1
        island[n][m] = number
        while bfs:
            x,y = bfs.popleft()
            for i in range(4):
                dx = x + d[i][0]
                dy = y + d[i][1]
                if 0<=dx<N and 0<=dy<M:
                    if ground[dx][dy] == 1 and island[dx][dy] == 0:
                        island[dx][dy] = number
                        bfs.append((dx,dy))

root = [i for i in range(number + 1)]
def find(k,r):
    while k != r[k]: k = r[k]
    return k

bridge = []
for i in range(N):
    last = island[i][0]
    dist = 0
    for j in range(1,M):
        if last == 0:
            if island[i][j] > 0:
                last = island[i][j]
        elif island[i][j] == 0:
            dist += 1
        elif dist > 0:
            if dist > 1:
                bridge.append((dist, last, island[i][j]))
            last = island[i][j]
            dist = 0

for i in range(M):
    last = island[0][i]
    dist = 0
    for j in range(1,N):
        if last == 0:
            if island[j][i] > 0:
                last = island[j][i]
        elif island[j][i] == 0:
            dist += 1
        elif dist > 0:
            if dist > 1:
                bridge.append((dist, last, island[j][i]))
            last = island[j][i]
            dist = 0

bridge.sort(reverse=True)

count = 0
cost = 0
while bridge and count < number - 1:
    d,a,b = bridge.pop()
    root_a = find(a,root)
    root_b = find(b,root)
    if root_a == root_b: continue
    if root_a < root_b:
        root[root_b] = root_a
    else:
        root[root_a] = root_b
    count += 1
    cost += d

linked = True
for i in range(2, number+1):
    if find(i,root) != find(i-1,root):
        linked = False
        break

if linked:
    print(cost)
else:
    print(-1)