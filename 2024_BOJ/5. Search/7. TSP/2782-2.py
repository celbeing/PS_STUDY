# 2782: 로맨틱 왕(brute-force)
import sys
from collections import deque
input = sys.stdin.readline

inf = 400_000
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = int(input())

def TSP(now, visit, depth, time):
    ret = 0
    bit = 1
    if depth < gift_count:
        for i in range(1, gift_count):
            bit <<= 1
            if visit & bit: continue
            new_time = time + (link[now][i] * depth)
            if new_time > limit: continue
            ret = max(ret, TSP(i, visit | bit, depth + 1, new_time))

    queen_time = time + (link[now][gift_count] * depth)
    if queen_time <= limit:
        ret = max(ret, depth - 1)
    return ret

for _ in range(t):
    h, w, limit = map(int, input().split())
    city = [list(input().strip()) for _ in range(h)]

    # 좌표 확인
    gift = deque()
    gift_cor = dict()
    gift_count = 1
    kx, ky = 0, 0
    qx, qy = 0, 0
    check_king = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if city[i][j] == 'K':
                kx, ky = i, j
                gift_cor[(i, j)] = 0
                bfs_king = deque([(i, j)])
                check_king[i][j] = 1
                while bfs_king:
                    x, y = bfs_king.popleft()
                    for k in range(4):
                        dx, dy = x + d[k][0], y + d[k][1]
                        if 0 <= dx < h and 0 <= dy < w and check_king[dx][dy] == 0 and city[dx][dy] != '#':
                            bfs_king.append((dx, dy))
                            check_king[dx][dy] = 1
            elif city[i][j] == 'Q':
                qx, qy = i, j
            elif city[i][j] == 'G':
                gift.append((i, j))
                gift_count += 1

    # K에서 닿지 않는 G는 그래프에서 제외
    real_gift_count = 1
    not_gift_count = 0
    gift.append((kx, ky))
    for i in range(gift_count - 1):
        gx, gy = gift.popleft()
        if check_king[gx][gy]:
            gift_cor[(gx, gy)] = real_gift_count
            gift.append((gx, gy))
            real_gift_count += 1
        else:
            not_gift_count += 1
    gift_count -= not_gift_count
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

    res = TSP(0, 1, 1, 0)
    print(res)