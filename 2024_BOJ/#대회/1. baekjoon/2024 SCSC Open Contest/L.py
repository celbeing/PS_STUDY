import sys
from collections import deque
input = sys.stdin.readline
N = int(input())
M = int(input())
blocks = [list(map(int,input().split())) for _ in range(N)]
ji = blocks[0][0]
X = int(input())
bfs = deque([(0,0)])
visit = [[0]*M for _ in range(N)]
visit[0][0] = 1
while bfs:
    x,y = bfs.popleft()
    if visit[-1][-1]: break
    for i in range(N):
        for j in range(M):
            if abs(x-i)+abs(y-j) > X: continue
            if visit[i][j]: continue
            if blocks[i][j] == ji:
                bfs.append((i,j))
                visit[i][j] = 1
if visit[-1][-1]: print("ALIVE")
else: print("DEAD")