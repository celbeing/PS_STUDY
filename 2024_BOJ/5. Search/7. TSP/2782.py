# 2782: 로맨틱 왕
import sys
from collections import deque
input = sys.stdin.readline
inf = 1000000
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = int(input())

def TSP(now, visit, depth):
    if tsp_dp[now][visit] == inf:
        bit = 1
        for i in range(1, gift_count):
            bit <<= 1
            if visit & bit: continue

            # k는 하위 탐색에서 반환된 소모 시간
            k = TSP(i, visit | bit, depth + 1)
            new_dist = link[now][i] + dist[i][visit | bit]
            k += new_dist
            # new_dist가 더해진 k는 현재 위치에서 예상되는 소모 시간

            # k가 현재 저장된 값보다 작은 경우
            # tsp_dp와 dist를 모두 갱신
            # k는 같은데 dist가 더 짧아질 수 있는 경우
            # dist만 갱신
            if k + (new_dist * depth)  < tsp_dp[now][visit] + (dist[now][visit] * depth):
                tsp_dp[now][visit] = k
                dist[now][visit] = new_dist
            elif k == tsp_dp[now][visit] and dist[now][visit] > new_dist:
                dist[now][visit] = new_dist

            '''
            # tsp_dp 갱신 조건 변경
            if k + new_dist < tsp_dp[now][visit] + dist[now][visit]:
                tsp_dp[now][visit] = k
                dist[now][visit] = new_dist
            '''
    return tsp_dp[now][visit]

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
                            link[i][j] = distance
                            link[j][i] = distance
                        bfs.append((dx, dy))

    tsp_dp = [[inf] * (1 << gift_count) for _ in range(gift_count + 1)]
    dist = [[0] * (1 << gift_count) for _ in range(gift_count + 1)]

    # Q로 돌아가는 경로 설정
    k = (1 << gift_count) - 1
    for i in range(gift_count):
        tsp_dp[i][k] = link[i][gift_count]
        dist[i][k] = link[i][gift_count]
    TSP(0, 1, 0)

    # K에서 출발하는 최적해 확인
    res = 0
    for i in range(1, 1 << gift_count, 2):
        if tsp_dp[0][i] <= limit:
            count = 0
            bit = 1
            for k in range(1, gift_count):
                bit <<= 1
                if not(i & bit): count += 1
            if res < count:
                res = count

    # G에서 출발하는 최적해에 K를 연결
    for i in range(1, gift_count):
        for j in range(1, 1 << gift_count, 2):
            if tsp_dp[i][j] + link[0][i] + dist[i][j] <= limit:
                count = 1
                bit = 1
                for k in range(1, gift_count):
                    bit <<= 1
                    if not (j & bit): count += 1
                if res < count:
                    res = count
    print(res)