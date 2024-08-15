#29754: 세상에는 많은 유튜버가 있고, 그중에서 버츄얼 유튜버도 존재한다.
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
ytb = dict()
for _ in range(N):
    name,day,s,e = map(str,input().split())
    h,m = map(int,s.split(":"))
    s = h*60+m
    h,m = map(int,e.split(":"))
    e = h*60+m
    ytb[name] = ytb.get(name,[0,0])
    ytb[name][0] += 1
    ytb[name][1] += e-s
real_ytb = []
for t in ytb:
    if ytb[t][0] >= 5 and ytb[t][1] >= 3600:
        real_ytb.append(t)
real_ytb.sort()
if real_ytb:
    for rtyb in real_ytb:
        print(rtyb)
else:
    print(-1)