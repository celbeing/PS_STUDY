#21736: 헌내기는 친구가 필요해
import sys
from collections import deque
input = sys.stdin.readline
d = [(1,0),(0,1),(-1,0),(0,-1)]
N,M = map(int,input().split())
campus = [list(input().rstrip()) for _ in range(N)]
check = [[0]*M for _ in range(N)]
bfs = deque()
count = 0
for i in range(N):
    for j in range(M):
        if campus[i][j] == 'I':
            check[i][j] = 1
            bfs.append((i,j))
            break
    if bfs: break

while bfs:
    x,y = bfs.popleft()
    for i in range(4):
        dx = x+d[i][0]
        dy = y+d[i][1]
        if 0<=dx<N and 0<=dy<M and not(check[dx][dy]) and campus[dx][dy] != 'X':
            bfs.append((dx, dy))
            check[dx][dy] = 1
            if campus[dx][dy] == 'P':
                count += 1

if count:
    print(count)
else:
    print("TT")