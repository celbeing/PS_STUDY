import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
W = list(map(int,input().split()))

total = 0
high = [0]*(N+1)
for i in range(N):
    total += W[i]
    if high[A[i]] < W[i]: high[A[i]] = W[i]
for i in range(1,N+1):
    total -= high[i]
print(total)