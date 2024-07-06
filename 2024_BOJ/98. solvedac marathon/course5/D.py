import sys
input = sys.stdin.readline
N,M = map(int,input().split())
check = dict()
style = []

for _ in range(N):
    a,b = map(str,input().split())
    if b in check: continue
    check[b] = a
    style.append([a,int(b)])
style.sort(key=lambda x:x[1])

def bin(k):
    s,e=0,len(style)
    while s<e:
        m = (s+e)//2
        if style[m][1] >= k: e = m
        else: s = m+1
    return e

for _ in range(M):
    print(style[bin(int(input()))][0])