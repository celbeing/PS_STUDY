#9370: 미확인 도착지
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
inf = 1e9
T=int(input())

def dijk(s):
    q = []
    distance = [inf]*(n+1)
    heappush(q,(0,s))
    distance[s] = 0

    while q:
        now, node = heappop(q)
        if distance[node] < now:
            continue
        for weight, next in graph[node]:
            new = now + weight

            if distance[next] == new:
                heappush(q, (new, next))
            elif distance[next] > new:
                distance[next] = new
                heappush(q, (new, next))

'''
def case():
    n,m,t = map(int,input().split())
    s,g,h = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    distance = [inf] * (n+1)
    thru = [0] * (n+1)
    destination = []
    for j in range(m):
        a,b,d = map(int,input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))
    for j in range(t):
        destination.append(int(input()))
    destination.sort()

    distance[s] = 0
    heap = []
    heapq.heappush(heap,(0,s,0))

    while heap:
        now, node = heapq.heappop(heap)
        if distance[node] < now:
            continue
        for weight, next in graph[node]:
            new = now + weight
            if (node == g and next == h) or (node == h and next == g):
                passed = 1

            if distance[next] == new and passed == 1 and thru[next] == 0:
                thru[next] = passed
                heapq.heappush(heap,(new,next,passed))
            elif distance[next] > new:
                distance[next] = new
                thru[next] = passed
                heapq.heappush(heap,(new,next,passed))

    result = []
    for j in destination:
        if thru[j] == 1:
            result.append(j)
    print(*result)
'''

for t in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    destination = []

    for j in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((d, b))
        graph[b].append((d, a))
    for j in range(t):
        destination.append(int(input()))
    destination.sort()