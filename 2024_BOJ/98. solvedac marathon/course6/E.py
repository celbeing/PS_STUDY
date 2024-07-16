import sys
input = sys.stdin.readline
N,K = map(int,input().split())
A = list(map(int,input().split()))
R = [list(map(int,input().split())) for _ in range(K)]
M = [list(map(int,input().split())) for _ in range(K)]
result = 0

def givecan(k,sat):
    global result
    if k == K:
        if result < sat:
            result = sat
        return
    for i in range(N):
        if A[i] == 0:
            continue
        for j in range(N):
            if (i == j and A[j] < 2) or A[j] == 0:
                continue
            A[i] -= 1
            A[j] -= 1
            givecan(k+1, sat+R[k][i]+M[k][j])
            A[i] += 1
            A[j] += 1

givecan(0,0)
print(result)