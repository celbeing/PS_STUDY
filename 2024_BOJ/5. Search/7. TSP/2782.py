# 2782: 로맨틱 왕
import sys
from collections import deque
input = sys.stdin.readline
inf = int(1e9)
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = int(input())

def TSP(now, visit):
    if tsp_dp[now][visit] == inf:
        for i in range(1, gift_count):
            if link[now][i] == inf or visit & 1 << i: continue

            k = TSP(i, visit | 1 << i) + link[now][i] + dist[i][visit | 1 << i]
            if k < tsp_dp[now][visit]:
                tsp_dp[now][visit] = k
                dist[now][visit] = dist[i][visit | 1 << i] + link[now][i]
    return tsp_dp[now][visit]

for _ in range(t):
    h, w, limit = map(int, input().split())
    city = [list(input().strip()) for _ in range(h)]

    # 좌표 확인
    gift = [(0, 0)]
    gift_cor = dict()
    gift_count = 1
    qx, qy = 0, 0
    for i in range(h):
        for j in range(w):
            if city[i][j] == 'K':
                gift[0] = (i, j)
                gift_cor[(i, j)] = 0
            elif city[i][j] == 'Q':
                qx, qy = i, j
            elif city[i][j] == 'G':
                gift.append((i, j))
                gift_cor[(i, j)] = gift_count
                gift_count += 1
    gift.append((qx, qy))
    gift_cor[(qx, qy)] = gift_count
    link = [[inf] * (gift_count + 1) for _ in range(gift_count + 1)]

    # 거리 확인
    bfs = deque()
    for i in range(gift_count):
        check = [[0] * w for _ in range(h)]
        bfs.append((gift[i]))
        check[bfs[0][0]][bfs[0][1]] = 1
        distance = 1
        while bfs:
            roop_count = len(bfs)
            for _ in range(roop_count):
                x, y = bfs.popleft()
                for k in range(4):
                    dx, dy = x + d[k][0], y + d[k][1]
                    if 0 <= dx < h and 0 <= dy < w and city[dx][dy] != '#'  and check[dx][dy] == 0:
                        check[dx][dy] = 1
                        if city[dx][dy] != '.':
                            j = gift_cor[(dx, dy)]
                            if j: link[i][j] = distance
                            if i: link[j][i] = distance
                        bfs.append((dx, dy))
            distance += 1
    tsp_dp = [[inf] * (1 << gift_count + 1) for _ in range(gift_count + 1)]
    dist = [[0] * (1 << gift_count + 1) for _ in range(gift_count + 1)]

    # Q로 돌아가는 경로 설정
    k = 1 << gift_count
    k -= 1
    for i in range(gift_count):
        tsp_dp[i][k] = link[i][gift_count]
        dist[i][k] = link[i][gift_count]
    link[0][0] = 0
    TSP(0, 1)

    res = 0

    for i in range(gift_count):
        for j in range(1, 1 << gift_count, 2):
            if tsp_dp[i][j] + link[0][i] + (dist[i][j] if i else 0) <= limit:
                count = 0
                for k in range(1, gift_count):
                    if not (j & (1 << k)): count += 1
                if res < count: res = count
    print(res)