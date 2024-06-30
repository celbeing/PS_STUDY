import sys
input = sys.stdin.readline
n,k = map(int,input().split())
light = [tuple(map(int,input().split())) for _ in range(k)]
light.sort()
time = 0
now = 0
for x,t,s in light:
    time += x-now
    now = x
    if ((time-s)//t)&1:
        time += t-((time-s)%t)
print(time+n-now)