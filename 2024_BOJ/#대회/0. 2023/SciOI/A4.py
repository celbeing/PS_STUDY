# 순열 그래프(graph)
import sys
input = sys.stdin.readline
N,M = map(int,input().split())
mod = 1000000007
tree = dict()
for i in range(1,N+1):
    tree[i] = []
for n in range(1,N):
    u,v = map(int,input().split())
    tree[u].append(v)
    tree[v].append(u)