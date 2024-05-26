# 14750: Jerry and Tom
import sys
input = sys.stdin.readline
n,k,h,m = map(int,input().split())
corner = [tuple(map(int,input().split())) for _ in range(n)]
hole = [tuple(map(int,input().split())) for _ in range(h)]
T = m+h+2

graph = [[] for _ in range(T)]
capa = [{} for _ in range(T)]
flow = [{} for _ in range(T)]


def connect(u,v,f = 1):
    graph[u].append(v)
    graph[v].append(u)
    capa[u][v] = f
    capa[v][u] = 0
    flow[u][v] = 0
    flow[v][u] = 0
    return

def ccw(a,b,c):
    k = (a[1]-b[1])*(b[0]-c[0])-(a[0]-b[0])*(b[1]-c[1])
    if k > 0: return 1
    elif k == 0: return 0
    else: return -1

def cross(a,b,c,d):
    cross1 = ccw(a, b, c) * ccw(a, b, d)
    cross2 = ccw(c, d, a) * ccw(c, d, b)

    if cross1 == cross2 == 0:
        if b == c or
        elif (min(a[0], b[0]) <= max(c[0], d[0]) and min(c[0], d[0]) <= max(a[0], b[0]) and
                min(a[1], b[1]) <= max(c[1], d[1]) and min(c[1], d[1]) <= max(a[1], b[1])):
            return False
        else:
            return True
    else:
        if cross1 <= 0 and cross2 <= 0:
            return False
        else:
            return True

