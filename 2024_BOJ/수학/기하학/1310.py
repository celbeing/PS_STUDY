#1310: 달리기 코스
import sys
input = sys.stdin.readline
N = int(input())
column = [list(map(int,input().split())) for _ in range(N)]

def ccw(a, b, c):
    return (a[1]-b[1])*(b[0]-c[0])-(a[0]-b[0])*(b[1]-c[1])
def calipers(dots):
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
    
    convex = left[:-1] + right[:-1]
    n = len(convex)
    l,r = 0,0
    for i in range(n):
        if convex[i][0] < convex[l][0]: l = i
        if convex[i][0] > convex[r][0]: r = i
    peek = (convex[l][0]-convex[r][0])**2+(convex[l][1]-convex[r][1])**2
    for i in range(n):
        vec_l = [convex[(l+1)%n][0]-convex[l][0],convex[(l+1)%n][1]-convex[l][1]]
        vec_r = [convex[r][0]-convex[(r+1)%n][0],convex[r][1]-convex[(r+1)%n][1]]
        k = ccw([0,0],vec_l,vec_r)
        if k > 0:
            l = (l+1)%n
        else:
            r = (r+1)%n
        dist = (convex[l][0]-convex[r][0])**2+(convex[l][1]-convex[r][1])**2
        if peek < dist:
            peek = dist
    return peek

print(calipers(column))