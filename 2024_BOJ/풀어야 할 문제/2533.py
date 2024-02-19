#2533: 사회망 서비스(SNS)
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)
