#9370: 미확인 도착지
import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize
T=int(input())

for t in range(T):
    n,m,t=map(int,input().split())
    s,g,h=map(int, input().split())
    dist = [inf]*(n+1)
    thru = [0]*(n+1)
    graph = [[] for _ in range(n+1)]
    candidate = []
    for _ in range(m):
        a,b,d=map(int,input().split())
        graph[a].append((d,b))
        graph[b].append((d,a))
    for _ in range(t):
        candidate.append(int(input()))
    candidate.sort()

    dist[s] = 0
    hq = []
    heapq.heappush(hq, (0, s, 0))

    while hq:
        w, node, passed = heapq.heappop(hq)
        if dist[node] < w: continue
        thru[node] = passed
        for weight, next in graph[node]:
            newdist = w+weight
            if dist[next] > newdist:
                dist[next] = newdist
                if (node == g and next == h) or (node == h and next == g):
                    heapq.heappush(hq,(newdist,next,1))
                else:
                    heapq.heappush(hq, (newdist, next, passed))
            elif dist[next] == newdist and ((node == g and next == h) or (node == h and next == g) or passed == 1) and thru[next] == 0:
                heapq.heappush(hq, (newdist, next, 1))

    result = []
    for k in candidate:
        if thru[k] == 1:
            result.append(k)

    print(*result)