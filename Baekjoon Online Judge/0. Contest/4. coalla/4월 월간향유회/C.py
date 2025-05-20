# 23284: 모든 스택 수열
import sys
input = sys.stdin.readline
n = int(input())
d = []

def dfs(P,S,k):
    p = P[0:]
    s = S[0:]
    if k == n+1:
        while s: p.append(s.pop())
        print(*p)
        return
    if s:
        p.append(s.pop())
        dfs(p,s,k)
        s.append(p.pop())
    s.append(k)
    dfs(p,s,k+1)

dfs(([]),([1]),2)