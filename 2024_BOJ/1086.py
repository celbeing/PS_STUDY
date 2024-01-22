#1086: 박성원
import sys
N = int(input())
remain = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    remain[i][0] = int(input())
K = int(input())
for i in range(N):
    remain[i][0] %= K
    for j in range(1,N):
        remain[i][j] = (remain[i][j-1]*10)%K