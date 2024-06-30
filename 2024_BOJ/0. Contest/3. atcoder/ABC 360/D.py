import sys
from bisect import bisect_right, bisect_left
input = sys.stdin.readline

N,T = map(int,input().split())
S = list(input().rstrip())
X = list(map(int,input().split()))

R = []
L = []
for i in range(N):
    if S[i] == "1":
        R.append(X[i])
    else:
        L.append(X[i])

R.sort()
L.sort()

count = 0
if R and L:
    for r in R:
        count += bisect_right(L,r+T*2)
        count -= bisect_left(L,r)
print(count)