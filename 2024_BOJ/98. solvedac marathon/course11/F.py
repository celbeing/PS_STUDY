#30974: What's your ETA?
import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
Dis_Code = [0]+list(map(int,input().split()))
Bus_Edge = dict()
for _ in range(M):
    u,v,w = map(int,input().split())
    Bus_Edge[u] = Bus_Edge.get(u,{})
    Bus_Edge[u][v] = Bus_Edge[u].get(v,w)
    if Bus_Edge[u][v] > w: Bus_Edge[u][v] = w
    Bus_Edge[v] = Bus_Edge.get(v,{})
    Bus_Edge[v][u] = Bus_Edge[v].get(u,w)
    if Bus_Edge[v][u] > w: Bus_Edge[v][u] = w

sieve = [1]*10000001
sieve[0] = 0
sieve[1] = 0
for i in range(2,3163):
    if sieve[i]:
        for j in range(i*i,10000001,i):
            sieve[j] = 0

print("DONE")
bfs = deque([1])