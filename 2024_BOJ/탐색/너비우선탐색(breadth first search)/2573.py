#2573: 빙산
import sys
from collections import deque
input = sys.stdin.readline
d = [[0,1],[1,0],[0,-1],[-1,0]]

N,M = map(int,input().split())
sea = [list(map(int,input().split())) for _ in range(N)]

def iceberg(sea):
    queue = deque()
    count = 0
    check = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0:
                if not(queue):
                    queue.append((i,j))
                    check[i][j] = 1
                count += 1
    if count == 0:
        return -1
    before = count

    while queue:
        x,y = queue.popleft()
        count -= 1
        for i in range(4):
            dx = x+d[i][0]
            dy = y+d[i][1]
            if 0<=dx<N and 0<=dy<M:
                if check[dx][dy] == 0 and sea[dx][dy] > 0:
                    queue.append((dx,dy))
                    check[dx][dy] = 1
    return count

year = 0
queue = deque()
count = iceberg(sea)
while count == 0:
    year += 1
    for i in range(N):
        for j in range(M):
            if sea[i][j] > 0:
                for k in range(4):
                    di = i+d[k][0]
                    dj = j+d[k][1]
                    if 0<=di<N and 0<=dj<M and sea[di][dj] < 1:
                        queue.append((i,j))
    while queue:
        x,y = queue.popleft()
        sea[x][y] -= 1

    count = iceberg(sea)
if count == -1:
    print(0)
else:
    print(year)