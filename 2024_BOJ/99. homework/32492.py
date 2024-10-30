#32495: WALK
import sys
input = sys.stdin.readline
def solution():
    N, M = map(int, input().split())
    dist = [0] * (N + 1)
    crnt = [0] * (N + 1)
    road = [dict() for _ in range(N + 1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        road[a][b] = c
        road[b][c] = c
    for now in range(1, N + 1):
        for next in road[now]:
            if road[now][next] > crnt[next] and