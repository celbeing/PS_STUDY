import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
B = A[:]
for i in range(1,N): B[i] -= A[i-1]
B.append(int(1e10))
res = 0
cnt = 1
k = B[1]
for i in range(2,N+1):
    if B[i] == k:
        cnt += 1
    else:
        res += (cnt**2+cnt)//2
        k = B[i]
        cnt = 1
print(res+N)