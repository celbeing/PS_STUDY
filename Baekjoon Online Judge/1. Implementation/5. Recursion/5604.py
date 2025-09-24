# 5604: 問題３
import sys
input = sys.stdin.readline

def dfs(paper, now, route):
    if paper == 0:
        print(*route)
        return
    for i in range(min(paper, now), 0, -1):
        dfs(paper - i, i, route + [i])

n = int(input())
dfs(n, int(1e9), [])