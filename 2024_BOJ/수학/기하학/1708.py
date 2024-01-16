#1708: 볼록 껍질
import sys
input = sys.stdin.readline

N = int(input())
dot = [list(map(int,input().split())) for _ in range(N)]
dot.sort()

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

result = graham(dot)
print(len(result))