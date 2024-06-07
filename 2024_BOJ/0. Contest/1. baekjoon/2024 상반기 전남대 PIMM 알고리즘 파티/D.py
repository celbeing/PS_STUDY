#D: 육각타일미로 탈출기
import sys
from collections import deque
input = sys.stdin.readline
N,M,K = map(int,input().split())
d = [[(0,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0)],[(0,1),(1,1),(1,0),(0,-1),(-1,0),(-1,1)]]
bfs = deque([(0,0)])
check = [[-1]*M for _ in range(N)]
check[0][0] = 0
for _ in range(K):
    x,y = map(int,input().split())
    check[x][y] = -2

while bfs:
    x,y = bfs.popleft()
    if x == N-1 and y == M-1:
        break
    k = x%2
    for i in range(6):
        dx = x+d[k][i][0]
        dy = y+d[k][i][1]
        if 0<=dx<N and 0<=dy<M:
            if check[dx][dy] == -1:
                bfs.append((dx,dy))
                check[dx][dy] = check[x][y] + 1

print(check[N-1][M-1])