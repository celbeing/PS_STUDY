import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
s = list(input().rstrip())
S = [0]*N
for i in range(N):
    S[i] = ord(s[i])-ord('A')
for _ in range(Q):
    q,l,r = map(int,input().split())
    if q == 1:
        count = 1
        for i in range(l,r):
            if S[i] != S[i-1]:
                count += 1
        print(count)
    else:
        for i in range(l-1,r):
            S[i] += 1
            S[i] %= 26