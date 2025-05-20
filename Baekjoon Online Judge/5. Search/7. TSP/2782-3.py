# 2782: 로맨틱 왕
import sys
from collections import deque
input = sys.stdin.readline
inf = 1000000
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = int(input())

def TSP(now, visit, depth):
    if dp[now][visit] == inf:
        bit = 1
        for next in range(1, gift_count):
            bit <<= 1
            if visit & bit: continue
            k = TSP(next, visit | 1 << next, depth - 1) + dist[now][next] * depth
            o = dp[now][visit]
            dp[now][visit] = min(o, k)
    return dp[now][visit]

for _ in range(t):
    h, w, limit = map(int, input().split())
    city = [list(input().strip()) for _ in range(h)]

    # 좌표 확인
    gift = deque()
    gift_cor = dict()
    gift_count = 1
    kx, ky = 0, 0
    qx, qy = 0, 0
    check_queen = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if city[i][j] == 'Q':
                qx, qy = i, j
                gift_cor[(i, j)] = 0
                bfs_queen = deque([(i, j)])
                check_queen[i][j] = 1
                while bfs_queen:
                    x, y = bfs_queen.popleft()
                    for k in range(4):
                        dx, dy = x + d[k][0], y + d[k][1]
                        if 0 <= dx < h and 0 <= dy < w and check_queen[dx][dy] == 0 and city[dx][dy] != '#':
                            bfs_queen.append((dx, dy))
                            check_queen[dx][dy] = 1
            elif city[i][j] == 'K':
                kx, ky = i, j
            elif city[i][j] == 'G':
                gift.append((i, j))
                gift_count += 1

    # K에서 닿지 않는 G는 그래프에서 제외
    real_gift_count = 1
    not_gift_count = 0
    gift.append((qx, qy))
    for i in range(gift_count - 1):
        gx, gy = gift.popleft()
        if check_queen[gx][gy]:
            gift_cor[(gx, gy)] = real_gift_count
            gift.append((gx, gy))
            real_gift_count += 1
        else:
            not_gift_count += 1
    gift_count -= not_gift_count
    gift.append((kx, ky))
    gift_cor[(kx, ky)] = gift_count
    dist = [[inf] * (gift_count + 1) for _ in range(gift_count + 1)]

    # 거리 확인
    bfs = deque()
    for i in range(gift_count):
        check = [[0] * w for _ in range(h)]
        bfs.append((gift[i]))
        check[bfs[0][0]][bfs[0][1]] = 1
        distance = 0
        while bfs:
            distance += 1
            roop_count = len(bfs)
            for _ in range(roop_count):
                x, y = bfs.popleft()
                for k in range(4):
                    dx, dy = x + d[k][0], y + d[k][1]
                    if 0 <= dx < h and 0 <= dy < w and city[dx][dy] != '#'  and check[dx][dy] == 0:
                        check[dx][dy] = 1
                        if city[dx][dy] != '.':
                            j = gift_cor[(dx, dy)]
                            dist[i][j] = distance
                            dist[j][i] = distance
                        bfs.append((dx, dy))

    dp = [[inf] * (1 << gift_count) for _ in range(gift_count + 1)]

    # K에서 출발하는 경로 설정
    k = (1 << gift_count) - 1
    for i in range(gift_count):
        dp[i][k] = dist[i][gift_count]
    TSP(0, 1, gift_count)

    # Q로 도착하는 최적해 확인
    res = 0
    for i in range(1, 1 << gift_count, 2):
        if dp[0][i] <= limit:
            count = 0
            bit = 1
            for k in range(1, gift_count):
                bit <<= 1
                if not(i & bit): count += 1
            if res < count:
                res = count

    # G에서 출발하는 최적해에 Q를 연결
    # 선물 갯수 따져봐야 함
    for i in range(1, gift_count):
        for j in range(1 | (1 << i), 1 << gift_count, 2):
            gift_in_hand = 2
            for k in range(1, gift_count):
                if not(j & (1 << k)):
                    gift_in_hand += 1
            k = dp[i][j] + dist[0][i] * gift_in_hand
            if k <= limit:
                if res < gift_in_hand:
                    res = gift_in_hand - 1
    print(res)