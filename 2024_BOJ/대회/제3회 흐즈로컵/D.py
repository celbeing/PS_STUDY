#D: 자료 구조의 왕
import sys
input = sys.stdin.readline

n,m,q = map(int,input().split())
rem = n*m
grass = [[0 for _ in range(m+1)] for _ in range(n+1)]
for _ in range(q):
    o = list(map(int,input().split()))
    if o[0] == 1:
        dy,dx,y,x = o[1],o[2],o[3],o[4]
        while 0<y<=n and 0<x<=n:
            if grass[y][x] == 1:
                break
            else:
                grass[y][x] = 1
                rem -= 1
                x += dx
                y += dy
    elif o[0] == 2:
        print(grass[o[1]][o[2]])
    else:
        print(rem)