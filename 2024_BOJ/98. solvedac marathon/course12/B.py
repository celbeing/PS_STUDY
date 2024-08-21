#5623: 수열의 합
import sys
input = sys.stdin.readline
N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]
if N == 2: print(A[0][1]//2,A[0][1]//2)
else:
    res = [0]*N
    res[1] = (A[0][1]+A[1][2]-A[0][2])//2
    for i in range(N):
        if i == 1: continue
        res[i] = A[1][i]-res[1]
    print(*res)