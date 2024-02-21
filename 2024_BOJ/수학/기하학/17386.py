#17386: 선분 교차 1
import sys
input = sys.stdin.readline
p,q,r,s = map(int,input().split())
t,u,v,w = map(int,input().split())
a = (p,q)
b = (r,s)
c = (t,u)
d = (v,w)

def ccw(a,b,c):
    k = (a[1]-b[1])*(b[0]-c[0])-(a[0]-b[0])*(b[1]-c[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

cross1 = ccw(a,b,c)*ccw(a,b,d)
cross2 = ccw(c,d,a)*ccw(c,d,b)

if cross1 == cross2 == 0:
    if (a <= d and b >= c)or(a >= d and b <= c):
        print(1)
        exit()
else:
    if cross1 <= 0 and cross2 <= 0:
        print(1)
        exit()
print(0)