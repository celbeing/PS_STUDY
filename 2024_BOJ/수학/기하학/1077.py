#1077: 넓이
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
convexA = [list(map(int,input().split())) for _ in range(N)]
convexB = [list(map(int,input().split())) for _ in range(M)]

if N < 3 or M < 3:
    print(0)
    exit()

def ccw(a, b, c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

def cross(a,b,c,d):
    point = [1000,1000]
    if ccw(a,b,c) * ccw(a,b,d) < 0 and ccw(c,d,a) * ccw(c,d,b) < 0:
        if a[0] == b[0]:
            m2 = (c[1] - d[1]) / (c[0] - d[0])
            point[0] = a[0]
            point[1] = m2*(point[0]-c[0])+c[1]
        elif c[0] == d[0]:
            m1 = (a[1] - b[1]) / (a[0] - b[0])
            point[0] = c[0]
            point[1] = m1*(point[0]-a[0])+a[1]
        else:
            m1 = (a[1]-b[1])/(a[0]-b[0])
            m2 = (c[1]-d[1])/(c[0]-d[0])
            point[0] = (m1*a[0]-a[1]-m2*c[0]+c[1])/(m1-m2)
            point[1] = m1*(point[0]-a[0])+a[1]
    return point

def inside(poly, p):
    n = len(poly)-1
    p1 = poly[0]
    count = 0
    for i in range(1,n+1):
        p2 = poly[i]
        if p[1] > min(p1[1],p2[1]) and p[1] <= max(p1[1],p2[1]) and p[0] <= max(p1[0],p2[0]) and p1[1] != p2[1]:
            x = (p[1]-p1[1])*(p2[0]-p1[0])/(p2[1]-p1[1])+p1[0]
            if p1[0] == p2[0] or p[0] <= x:
                count += 1
        p1 = p2
    if count % 2 == 0:
        return False
    else:
        return True

def area(poly):
    poly.sort()
    result = 0
    left = []
    for p in poly:
        while len(left) >= 2 and ccw(left[-2],left[-1],p) <= 0:
            left.pop()
        left.append(p)
    for i in range(len(left)-1):
        result += (left[i+1][0]-left[i][0])*(left[i+1][1]+left[i][1])/2
    right = []
    for p in reversed(poly):
        while len(right) >= 2 and ccw(right[-2],right[-1],p) <= 0:
            right.pop()
        right.append(p)
    for i in range(len(right)-1):
        result += (right[i+1][0]-right[i][0])*(right[i+1][1]+right[i][1])/2
    return result

convexC = []
convexA.append(convexA[0])
convexB.append(convexB[0])
for i in range(N):
    if inside(convexB,convexA[i]):
        convexC.append(convexA[i])
    for j in range(M):
        p = cross(convexA[i],convexA[i+1],convexB[j],convexB[j+1])
        if p != [1000,1000]:
            convexC.append(p)
for i in range(M):
    if inside(convexA,convexB[i]):
        convexC.append(convexB[i])
areaC = area(convexC)
print(areaC)