#31712: 핑크빈 레이드
import sys
input = sys.stdin.readline
cu,du = map(int,input().split())
cd,dd = map(int,input().split())
cp,dp = map(int,input().split())
u,d,p = 0,0,0
H = int(input()) - (du+dd+dp)
t = 0
while H > 0:
    t += 1
    u += 1
    d += 1
    p += 1
    if u == cu:
        H -= du
        u = 0
    if d == cd:
        H -= dd
        d = 0
    if p == cp:
        H -= dp
        p = 0
print(t)