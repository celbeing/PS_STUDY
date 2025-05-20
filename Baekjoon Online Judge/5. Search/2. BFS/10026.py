#10026: 적록색약
import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
pic = [list(input().rstrip()) for _ in range(N)]
countA = 1
countB = 1
check = [[0]*N for _ in range(N)]
d = [(1,0),(0,1),(-1,0),(0,-1)]
bfs = deque([(0,0)])
check[0][0] = 1

while bfs:
    x,y = bfs.popleft()
    for i in range(4):
        dx = x+d[i][0]
        dy = y+d[i][1]
        if 0<=dx<N and 0<=dy<N and pic[x][y] == pic[dx][dy] and check[dx][dy] == 0:
            check[dx][dy] = 1
            bfs.append((dx,dy))
    if not(bfs):
        for i in range(N):
            for j in range(N):
                if check[i][j] == 0:
                    countA += 1
                    bfs.append((i,j))
                    check[i][j] = 1
                    break
            if bfs: break


bfs = deque([(0,0)])
check[0][0] = 0
while bfs:
    x,y = bfs.popleft()
    for i in range(4):
        dx = x+d[i][0]
        dy = y+d[i][1]
        if 0<=dx<N and 0<=dy<N and (pic[dx][dy] == pic[x][y] == 'B' or (pic[dx][dy] != 'B' and pic[x][y] != 'B')) and check[dx][dy] == 1:
            check[dx][dy] = 0
            bfs.append((dx,dy))
    if not(bfs):
        for i in range(N):
            for j in range(N):
                if check[i][j] == 1:
                    countB += 1
                    bfs.append((i,j))
                    check[i][j] = 0
                    break
            if bfs: break

print(countA,countB)