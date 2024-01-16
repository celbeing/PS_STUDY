#1708: 볼록 껍질
import sys
input = sys.stdin.readline

N = int(input())
dot = [list(map(int,input().split())) for _ in range(N)]
dot.sort()

def direction(a,b,c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])

    # 우회전
    if k > 0:
        return 1
    # 좌회전
    elif k < 0:
        return -1
    # 직선상
    else:
        return 0

def graham(n, dots):
    leftside = []
    leftside.append(dots[0])
    leftside.append(dots[1])
    for i in range(2,n):
        a = direction(leftside[-2],leftside[-1],dots[i])
        if a > 0:
            leftside.pop()
            leftside.append(dots[i])

    reversed(dots)
    rightside = []
    rightside.append(dots[0])
    rightside.append(dots[1])
    for i in range(2,n):
        a = direction(rightside[-2],rightside[-1],dots[i])
        if a > 0:
            rightside.pop()
            rightside.append(dots[i])

    while len(rightside) > 0:
        if leftside[-1] != rightside[0]:
            leftside.append(rightside[0])
            del rightside[0]
    return leftside

result = graham(N,dot)
print(*result)