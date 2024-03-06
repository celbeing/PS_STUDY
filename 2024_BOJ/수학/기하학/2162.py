#2162: 선분 그룹
import sys
input = sys.stdin.readline
N = int(input())
dots = [list(map(int,input().split())) for _ in range(N)]
root = [i for i in range(N)]

def ccw(a,b,c):
    k = (a[1]-b[1])*(b[0]-c[0])-(a[0]-b[0])*(b[1]-c[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

def cross(a,b,c,d):
    c1 = ccw(a,b,c)*ccw(a,b,d)
    c2 = ccw(c,d,a)*ccw(c,d,b)

    if c1 == c2 == 0:
        if min(a[0], b[0]) <= max(c[0], d[0]) and min(c[0], d[0]) <= max(a[0], b[0]) and min(a[1], b[1]) <= max(c[1], d[1]) and min(c[1], d[1]) <= max(a[1], b[1]):
            return True
        else:
            return False

    if c1 <= 0 and c2 <= 0:
        return True
    else:
        return False

def find(k,r):
    while k != r[k]: k = r[k]
    return k

for i in range(1, N):
    a = (dots[i][0], dots[i][1])
    b = (dots[i][2], dots[i][3])
    for j in range(i):
        c = (dots[j][0], dots[j][1])
        d = (dots[j][2], dots[j][3])

        if cross(a,b,c,d):
            rj = find(j,root)
            root[rj] = i

max = 1
group =dict()

for i in range(N):
    k = find(i,root)
    if k in group:
        group[k] += 1
        if group[k] > max:
            max = group[k]
    else:
        group[k] = 1

print(len(group))
print(max)