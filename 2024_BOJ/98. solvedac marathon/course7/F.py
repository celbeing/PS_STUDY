import sys
input = sys.stdin.readline
N,M = map(int,input().split())
ss = list(map(int,input().split()))
es = list(map(int,input().split()))
c1 = []
c2 = []

def count(a,b):
    p,q = 0,0
    l,o = 0,0
    for i in range(N):
        if a[i]: l += 1
        else: o += 1
        if b[i]: l -= 1
        else: o -= 1
    ret = 0
    if l == o == 0:
        while p<N and q<N:
            while p<N and a[p] == 0: p += 1
            while q<N and b[q] == 0: q += 1
            if p<N and q<N:
                ret += abs(p-q)
                p += 1
                q += 1
        return ret
    else:
        return 99

for i in range(M):
    if i&1:
        c1 += [0]*es[i]
        c2 += [1]*es[i]
    else:
        c1 += [1]*es[i]
        c2 += [0]*es[i]

print(min(count(ss,c1),count(ss,c2)))