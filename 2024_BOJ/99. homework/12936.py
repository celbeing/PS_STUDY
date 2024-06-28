# 12936: 영웅은 죽지 않아요
import sys
input = sys.stdin.readline
from collections import deque

N,M = map(int,input().split())
rev = list(map(int,input().split()))
graph = [[] for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)