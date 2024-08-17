#29754: 세상에는 많은 유튜버가 있고, 그중에서 버츄얼 유튜버도 존재한다.
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
ytb = dict()
for _ in range(N):
    name,day,s,e = map(str,input().split())
    day = int(day)
    h,m = map(int,s.split(":"))
    s = h*60+m
    h,m = map(int,e.split(":"))
    e = h*60+m
    ytb[name] = ytb.get(name,[[0]*((M+6)//7) for _ in range(2)])
    ytb[name][0][(day-1)//7] += e-s
    ytb[name][1][(day-1)//7] += 1
real_ytb = []
for t in ytb:
    if min(ytb[t][1]) >= 5 and min(ytb[t][0]) >= 3600:
        real_ytb.append(t)
real_ytb.sort()
if real_ytb:
    for rtyb in real_ytb:
        print(rtyb)
else:
    print(-1)