# 5766: 할아버지는 유명해!
import sys
input = sys.stdin.readline
def solution():
    while True:
        N, M = map(int, input().split())
        if N == M == 0: break
        rank = dict()
        for _ in range(N):
            weekly = list(map(int, input().split()))
            for n in weekly:
                rank[n] = rank.get(n, 0) + 1
        total_rank = list(rank.items())
        total_rank.sort(key = lambda x: (-x[1], x[0]))
        k = 1
        res = []
        while k < len(total_rank) and total_rank[k][1] == total_rank[1][1]:
            res.append(total_rank[k][0])
            k += 1
        print(*res)
solution()