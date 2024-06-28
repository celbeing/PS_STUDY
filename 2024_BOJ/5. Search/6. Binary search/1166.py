# 1166: 선물
import sys
input = sys.stdin.readline
N,L,W,H = map(int,input().split())

s,e = 0,min(L,min(W,H))+1
while s < e:
    m = (s+e)/2
    if s == m or e == m: break
    r = (L//m)*(W//m)*(H//m)
    if r < N: e = m
    else: s = m
r = (L//m)*(W//m)*(H//m)
print(s)