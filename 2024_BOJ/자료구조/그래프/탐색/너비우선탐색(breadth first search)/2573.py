#2573: 빙산
import sys
from collections import deque
input = sys.stdin.readline().rstrip
d = [[0,1],[1,0],[0,-1],[-1,0]]

N,M = map(int,input().split())
sea = [list(map(int,input().split())) for _ in range(N)]

def iceburg(sea):
    queue = deque()
    check = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if queue: break
            if sea[i][j] != 0:
                queue.append([i,j])
        if queue: break

    
    while queue:
