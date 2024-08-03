import sys
input = sys.stdin.readline
N,M= map(int,input().split())
A = sorted(list(map(int,input().split())))
S = A[:]
for i in range(1,N): S[i] += S[i-1]

s,e = 0,N
while s<e:
    m = (s+e)//2
    if S[m] + (N-m-1)*A[m] < M: s = m+1
    else: e = m

if e == N : print("infinite")
else:
    b = A[e] + (M - (S[e] + (N - e - 1) * A[e])) // (N - e)
    if b == A[-1]: print("infinite")
    else: print(b)