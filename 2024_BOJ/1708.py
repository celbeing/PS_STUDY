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

def graham(dots):
    leftside = []


    rightside = []

