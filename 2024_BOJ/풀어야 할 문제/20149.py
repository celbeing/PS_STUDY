#20149: 선분 교차 3
import sys
input = sys.stdin.readline
p,q,r,s = map(int,input().split())
t,u,v,w = map(int,input().split())
a = (p,q)
b = (r,s)
c = (t,u)
d = (v,w)

minabx = min(a[0], b[0])
minaby = min(a[1], b[1])
maxabx = max(a[0], b[0])
maxaby = max(a[1], b[1])
mincdx = min(c[0], d[0])
mincdy = min(c[1], d[1])
maxcdx = max(c[0], d[0])
maxcdy = max(c[1], d[1])

def ccw(a,b,c):
    k = (a[1]-b[1])*(b[0]-c[0])-(a[0]-b[0])*(b[1]-c[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

def sol():
    m_ab,m_cd,k_ab,k_cd = 0,0,0,0
    h_ab,h_cd = False,False
    x,y = 0,0

    if a[0] == b[0]:
        x = a[0]
        h_ab = True
    else:
        m_ab = (a[1] - b[1]) / (a[0] - b[0])
        k_ab = a[1] - (m_ab * a[0])

    if c[0] == d[0]:
        x = c[0]
        h_cd = True
    else:
        m_cd = (c[1] - d[1]) / (c[0] - d[0])
        k_cd = c[1] - (m_cd * c[0])

    if h_ab:
        y = m_cd * x + k_cd
    elif h_cd:
        y = m_ab * x + k_ab
    else:
        x = (k_cd - k_ab)/(m_ab - m_cd)
        y = m_ab * x + k_ab

    if ccw(a,b,c) == 0 and ccw(a,b,d) != 0:
        x,y = c
    elif ccw(a,b,c) != 0 and ccw(a,b,d) == 0:
        x,y = d
    elif ccw(c,d,a) == 0 and ccw(c,d,b) != 0:
        x,y = a
    elif ccw(c,d,a) != 0 and ccw(c,d,b) == 0:
        x,y = b

    if minabx <= x <= maxabx and mincdx <= x <= maxcdx and minaby <= y <= maxaby and mincdy <= y <= maxcdy:
        print(x,y)
    return

cross1 = ccw(a,b,c)*ccw(a,b,d)
cross2 = ccw(c,d,a)*ccw(c,d,b)

if ccw(a,b,c) == ccw(a,b,d) == 0:
    if minabx <= maxcdx and mincdx <= maxabx and minaby <= maxcdy and mincdy <= maxaby:
        print(1)
        if minabx != maxabx:
            if minabx == maxcdx:
                if a[0] > b[0]:
                    print(*b)
                else:
                    print(*a)
            elif maxabx == mincdx:
                if a[0] > b[0]:
                    print(*a)
                else:
                    print(*b)
        else:
            if minaby == maxcdy:
                if a[1] > b[1]:
                    print(*b)
                else:
                    print(*a)
            elif maxaby == mincdy:
                if a[1] > b[1]:
                    print(*a)
                else:
                    print(*b)
    else:
        print(0)
else:
    if cross1 <= 0 and cross2 <= 0:
        print(1)
        sol()
    else:
        print(0)