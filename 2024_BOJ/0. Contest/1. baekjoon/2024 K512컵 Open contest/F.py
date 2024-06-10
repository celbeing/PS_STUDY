import sys
input = sys.stdin.readline

def dist(x,y):
    return abs(E[0]-x)+abs(E[1]-y)

def binary_search(x,y):
    s,e = 0,N
    while s < e:
        m = (s+e)//2
        if item[m] > (x,y): e = m
        elif item[m] < (x,y): s = m+1
        else: return True
    return False

N,K = map(int,input().split())
item = [tuple(map(int,input().split())) for _ in range(N)]
item.sort()
E = tuple(map(int,input().split()))
sta = min(K+1,dist(0,0))
for ax,ay in item:
    sta = min(sta, dist(ax,ay)+2)
    bx = E[0]-ax
    by = E[1]-ay
    if sta > 4:
        if binary_search(bx,by): sta = 4
    if sta > 5:
        if binary_search(bx,by+1): sta = 5
        elif binary_search(bx,by-1): sta = 5
        elif binary_search(bx+1,by): sta = 5
        elif binary_search(bx-1,by): sta = 5

if sta == K+1: print(-1)
else: print(sta)