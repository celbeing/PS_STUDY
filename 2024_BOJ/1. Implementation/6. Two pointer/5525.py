#5525: IOIOI
import sys
input = sys.stdin.readline
N=int(input())
M=int(input())
S=list(input().rstrip())+['O']
s,e,r=0,0,0
while s < M and e < M:
    if S[s] == 'I':
        e = s
        while e < M and S[e] != S[e+1]:
            e += 1
        l = e-s+1
        if not(l & 1): l -= 1
        l //= 2
        if l >= N: r += l-N+1
        s = e+1
    else:
        s += 1
print(r)