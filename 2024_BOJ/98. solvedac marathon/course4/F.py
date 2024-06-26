import sys
input = sys.stdin.readline
N,K = map(int,input().split())
X = sorted([int(input()) for _ in range(N)])
R = [0]*N
for i in range(1,N):
    R[i] = R[i-1]+(X[i]-X[i-1])*i
s,e = 0,N
while s < e:
    m = (s+e)//2
    if R[m] >= K: e = m
    elif R[m] < K: s = m+1
if s == N or R[s] > K: s -= 1

rem = K - R[s]
print(X[s]+rem//(s+1))