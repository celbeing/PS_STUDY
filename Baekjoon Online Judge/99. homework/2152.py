# 2152: 여행 계획 세우기
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n, m, s, t = map(int, input().split())
edge = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    edge[u].append(v)