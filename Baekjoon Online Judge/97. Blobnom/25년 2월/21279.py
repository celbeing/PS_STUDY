# 21279: 광부 호석
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
def solution():
    n, c = map(int, input().split())
    mine = []
    for _ in range(n):
        x, y, v = map(int, input().split())
        heappush(mine, (x, -y, v))

    res = 0
    cost = 0
    score = 0
    hoesuk = []
    cnt_x = 0
    cnt_y = 100000
    while mine:
        while mine and mine[0][0] == cnt_x:
            x, y, v = heappop(mine)
            if -y > cnt_y: continue
            heappush(hoesuk, (y, x, v))
            score += v
            cost += 1
        else:
            if mine:
                cnt_x = mine[0][0]

        while hoesuk and cost > c:
            cnt_y = -hoesuk[0][0]
            while hoesuk and hoesuk[0][0] == -cnt_y:
                y, x, v = heappop(hoesuk)
                score -= v
                cost -= 1
        else:
            if res < score:
                res = score
    print(res)
solution()