# 11377: 열혈강호 3
import sys
from collections import deque
inf = int(1e9)
input = sys.stdin.readline

n,m,K = map(int,input().split())
N = n*2; M = m*2
graph = [[]*(n+1)]

# 직원: 2~n+2; 일: N+2~N+m+2
capa = [[]*(N+M+3) for _ in range(N+M+3)]
flow = [[]*(N+M+3) for _ in range(N+M+3)]
for i in range(2,n+2):
    capa[1][i] = 2
    capa[i][i+n] = 2
for i in range(N+2,N+m+2):
    capa[i][i+m] = 1
    capa[i+m][N+M+2] = 1
capa[0][1] = n+K
for i in range(2,n+2):
    task = list(map(int,input().split()))
    for j in range(1,task[0]+1):
        graph[i+n+2][N+j+2] = 1
        