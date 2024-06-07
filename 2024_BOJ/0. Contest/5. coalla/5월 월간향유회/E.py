import sys
input = sys.stdin.readline
N = int(input())

def ccw(a,b,c):
    k = (a[1]-b[1])*(b[0]-c[0])-(a[0]-b[0])*(b[1]-c[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

def cross(a,b,c,d):
    cross1 = ccw(a,b,c)*ccw(a,b,d)
    cross2 = ccw(c,d,a)*ccw(c,d,b)
    if cross1 == cross2 == 0:
        print("LINE")
    else:
        x,y = 0.0,0.0
        if a[0] == b[0] and c[0] == d[0]:
            print("NONE")
            return
        elif a[1] == b[1] and c[1] == d[1]:
            print("NONE")
            return
        elif a[0] == b[0]:
            x = a[0]
            w2 = (c[1]-d[1])/(c[0]-d[0])
            c2 = (c[1]-w2*c[0])
            if w2 == 0:
                y = c2
            else:
                y = w2*x+c2
        elif c[0] == d[0]:
            x = c[0]
            w1 = (a[1]-b[1])/(a[0]-b[0])
            c1 = (a[1]-w1*a[0])
            if w1 == 0:
                y = c1
            else:
                y = w1*x+c1

        else:
            w1 = (a[1]-b[1])/(a[0]-b[0])
            w2 = (c[1]-d[1])/(c[0]-d[0])
            if w1 == w2:
                print("NONE")
                return
            c1 = (a[1]-w1*a[0])
            c2 = (c[1]-w2*c[0])
            x = (c2-c1)/(w1-w2)
            y = x*w1+c1
        print("POINT {:.2f} {:.2f}".format(x,y))

for _ in range(N):
    x1,y1,x2,y2,x3,y3,x4,y4 = map(int,input().split())
    a = (x1,y1)
    b = (x2,y2)
    c = (x3,y3)
    d = (x4,y4)
    cross(a,b,c,d)