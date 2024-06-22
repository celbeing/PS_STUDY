import sys
input = sys.stdin.readline
N = int(input())
H = list(map(int,input().split()))
high = [(0,int(1e9))]
A = [0]*(N+1)
for i in range(1,N+1):
    while H[i-1] > high[-1][1]: high.pop()
    A[i] = (i-high[-1][0])*H[i-1]+A[high[-1][0]]
    high.append((i,H[i-1]))
for i in range(1,N+1): A[i] += 1
print(*A[1:])