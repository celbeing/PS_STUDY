# 1072: 게임
import sys
input = sys.stdin.readline
X,Y = map(int,input().split())
Z = Y*100//X
if Z >= 99:
    print(-1)
    exit()
s,e = 0,int(1e12)
while s < e:
    m = (s+e)//2
    r = (Y+m)*100//(X+m)
    if Z == r:
        s = m+1
    else:
        e = m
print(s)