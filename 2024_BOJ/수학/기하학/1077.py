#1077: 넓이
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
convexA = [[list(map(int,input().split()))] for _ in range(N)]
convexB = [[list(map(int,input().split()))] for _ in range(M)]

def ccw(a, b, c):
    k = (b[1]-a[1])*(c[0]-b[0])-(b[0]-a[0])*(c[1]-b[1])
    if k > 0: return 1
    elif k < 0: return -1
    else: return 0

def isinside(poly, p):
    