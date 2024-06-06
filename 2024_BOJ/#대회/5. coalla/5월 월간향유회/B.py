import sys
input = sys.stdin.readline

N,M = map(int,input().split())
pic = [[M]*101 for _ in range(101)]
for _ in range(N):
    a,b,c,d = map(int,input().split())
    for x in range(a,c+1):
        for y in range(b,d+1):
            pic[x][y] -= 1
r = 0
for x in range(1,101):
    for y in range(1,101):
        if pic[x][y]<0: r+=1

print(r)