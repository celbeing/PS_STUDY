# 14750: Jerry and Tom
import sys
from collections import deque
input = sys.stdin.readline

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

def cross(m, h, a, b):
    if h == a or h == b: return True
    v1 = ccw(m,h,a)
    v2 = ccw(m,h,b)
    v3 = ccw(a,b,m)
    v4 = ccw(a,b,h)
    cross1 = v1*v2
    cross2 = v3*v4

    # 네 점이 일직선 상에 있을 때
    if cross1 == cross2 == 0:
        # 쥐구명이 모서리에 있는 경우
        l = [m, h, a, b]
        if m <= h: l.sort()
        else: l.sort(reverse=True)
        if not((l[0] == m and l[1] == h) or (l[2] == m and l[3] == h)):
            return False
        else:
            return True
    else:
        if v4 == 0:
            return True
        elif cross1 <= 0 and cross2 <= 0:
            return False
        else:
            return True

def lv_graph():
    level = [-1]*(m+h+2)
    level[0] = 0
    bfs = deque([0])
    while bfs:
        now = bfs.popleft()
        for next in graph[now]:
            if level[next] == -1 and capa[now][next] - flow[now][next] > 0:
                level[next] = level[now]+1
                bfs.append(next)
    return level

def dinic(now,cut):
    if now == m+h+1: return cut

    for i in range(work[now],len(graph[now])):
        next = graph[now][i]
        residual = capa[now][next] - flow[now][next]
        if level[now]+1 == level[next] and residual > 0:
            f = dinic(next,min(cut,residual))
            if f > 0:
                flow[now][next] += f
                flow[next][now] -= f
                return f
        work[now] += 1
    return 0

n,k,h,m = map(int,input().split())
corner = [tuple(map(int,input().split())) for _ in range(n)]
hole = [tuple(map(int,input().split())) for _ in range(h)]
T = m+h+2

graph = [[] for _ in range(T)]
capa = [{} for _ in range(T)]
flow = [{} for _ in range(T)]

for i in range(1,h+1):
    connect(m+i,m+h+1,k)
for i in range(1,m+1):
    mouse = tuple(map(int,input().split()))
    connect(0,i)
    for j in range(h):
        insight = True
        for w in range(n):
            a = corner[w-1]
            b = corner[w]
            if cross(mouse,hole[j],a,b):
                continue
            else:
                insight = False
                break
        if insight: connect(i,m+j+1)

hidden = 0
while True:
    level = lv_graph()
    if level[-1] == -1: break

    work = [0]*(m+h+2)
    f = dinic(0,int(1e9))
    if f == 0: break
    else: hidden += f

if hidden == m: print("Possible")
else: print("Impossible")