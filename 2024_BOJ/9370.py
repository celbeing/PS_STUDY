#9370: 미확인 도착지
import sys
import heapq
input = sys.stdin.readline
inf = sys.maxsize
T=int(input())

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
        now, node, passed = heapq.heappop(heap)
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

for t in range(T):
    case()