import sys
input = sys.stdin.readline
N,K = map(int,input().split())
A = list(map(int,input().split()))
prx = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(i,N):
        prx[i][j] += A[j]
