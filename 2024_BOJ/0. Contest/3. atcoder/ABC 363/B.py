import sys
input = sys.stdin.readline
N,T,P = map(int,input().split())
L = list(map(int,input().split()))
D = [0]*N
for i in range(N):
    D[i] = T-L[i]
D.sort()
if D[P-1] > 0: print(D[P-1])
else: print(0)