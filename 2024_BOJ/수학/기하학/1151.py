#1151: 그림자
import sys
input = sys.stdin.readline

xyz = list(map(int,input().split()))
x,y,z = map(int,input().split())
X = [xyz[0],xyz[0],xyz[0],xyz[0],xyz[3],xyz[3],xyz[3],xyz[3]]
Y = [xyz[1],xyz[1],xyz[4],xyz[4],xyz[1],xyz[1],xyz[4],xyz[4]]
Z = [xyz[2],xyz[5],xyz[2],xyz[5],xyz[2],xyz[5],xyz[2],xyz[5]]
shade = []
for i in range(8):
    a,b,c = X[i],Y[i],Z[i]
    if c >= z: continue
    shade.append((x-(z*(x-a)/(z-c)), y-(z*(y-b)/(z-c))))

if len(shade) < 8:
    print(-1)
    exit()

def ccw(a, b, c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

def graham(dots):
    dots.sort()

    left = []
    for p in dots:
        while len(left) >= 2 and ccw(left[-2],left[-1],p) <= 0:
            left.pop()
        left.append(p)
    right = []
    for p in reversed(dots):
        while len(right) >= 2 and ccw(right[-2],right[-1],p) <= 0:
            right.pop()
        right.append(p)

    return left[:-1]+right[:-1]

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

convex = graham(shade)
result = area(convex)
print(result)