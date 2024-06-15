import sys
input = sys.stdin.readline
N,M = map(int,input().split())
A = sorted(list(map(int,input().split())))
B = sorted(list(map(int,input().split())))
count = 0
k = 0
for i in range(M):
    while k < N and B[i] > A[k]: k += 1
    if k == N:
        count = -1
        break
    count += A[k]
    k += 1
print(count)