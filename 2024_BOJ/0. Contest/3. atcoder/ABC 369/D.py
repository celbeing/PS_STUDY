import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split()))
o,e = [0]*N,[0]*N
o[0] = A[0]
for i in range(1,N):
    o[i] = max(o[i-1],e[i-1]+A[i])
    e[i] = max(e[i-1],o[i-1]+A[i]*2)
print(max(o[-1],e[-1]))