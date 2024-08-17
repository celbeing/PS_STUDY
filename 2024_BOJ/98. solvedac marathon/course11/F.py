#30974: What's your ETA?
import sys
from heapq import heappush,heappop
input = sys.stdin.readline
inf = int(1e12)
N,M = map(int,input().split())
Dis_Code = [0]+list(map(int,input().split()))
Bus_Edge = dict()

sieve = [1]*10000001
sieve[0] = 0
sieve[1] = 0
for i in range(2,3163):
    if sieve[i]:
        for j in range(i*i,10000001,i):
            sieve[j] = 0

for _ in range(M):
    u,v,w = map(int,input().split())
    if sieve[Dis_Code[u]+Dis_Code[v]]:
        Bus_Edge[u] = Bus_Edge.get(u,{})
        Bus_Edge[u][v] = Bus_Edge[u].get(v,w)
        if Bus_Edge[u][v] > w: Bus_Edge[u][v] = w
        Bus_Edge[v] = Bus_Edge.get(v,{})
        Bus_Edge[v][u] = Bus_Edge[v].get(u,w)
        if Bus_Edge[v][u] > w: Bus_Edge[v][u] = w

dist = [inf]*(N+1)
bfs = [(0,1)]
dist[1] = 0
while bfs:
    d,now = heappop(bfs)
    if now == N: break
    if dist[now] < d: continue
    if now in Bus_Edge:
        for next in Bus_Edge[now]:
            next_d = d + Bus_Edge[now][next]
            if dist[next] > next_d:
                heappush(bfs,(next_d,next))
                dist[next] = next_d

if dist[N] == inf:
    print("Now where are you?")
else:
    print(dist[N])