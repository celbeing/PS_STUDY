import sys
input = sys.stdin.readline
N,K = map(int,input().split())
d = N-K
A = sorted(list(map(int,input().split())))
min = A[-1]-A[0]
for i in range(K+1):
    p = A[i+d-1]-A[i]
    if min > p:
        min = p
print(min)