#14620: 꽃길
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    d = [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1)]
    cost = [list(map(int, input().split())) for _ in range(N)]
    res = 3000
    visit = [[0] * N for _ in range(N)]
    for i in range(N**2):
        ix = i // N
        iy = i % N
        for t in range(5):
            ixt = ix + d[t][0]
            iyt = iy + d[t][1]
            if 0<= ixt < N and 0 <= iyt < N and visit[ixt][iyt] == 0:
                continue
            break
        else:
            for t in range(5):
                visit[ix + d[t][0]][iy + d[t][1]] = 1
            for j in range(i + 1, N**2):
                jx = j // N
                jy = j % N
                for t in range(5):
                    jxt = jx + d[t][0]
                    jyt = jy + d[t][1]
                    if 0 <= jxt < N and 0 <= jyt < N and visit[jxt][jyt] == 0:
                        continue
                    break
                else:
                    for t in range(5):
                        visit[jx + d[t][0]][jy + d[t][1]] = 1
                    for k in range(j + 1, N**2):
                        kx = k // N
                        ky = k % N
                        for t in range(5):
                            kxt = kx + d[t][0]
                            kyt = ky + d[t][1]
                            if 0 <= kxt < N and 0 <= kyt < N and visit[kxt][kyt] == 0:
                                continue
                            break
                        else:
                            p = 0
                            for t in range(5):
                                p += cost[ix + d[t][0]][iy + d[t][1]]
                                p += cost[jx + d[t][0]][jy + d[t][1]]
                                p += cost[kx + d[t][0]][ky + d[t][1]]
                            if p < res:
                                res = p
                    for t in range(5):
                        visit[jx + d[t][0]][jy + d[t][1]] = 0
            for t in range(5):
                visit[ix + d[t][0]][iy + d[t][1]] = 0
    print(res)
solution()