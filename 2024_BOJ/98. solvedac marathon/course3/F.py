import sys
from heapq import heappush,heappop
input = sys.stdin.readline
xs,ys = map(int,input().split())
xe,ye = map(int,input().split())
tel1 = list(map(int,input().split()))
tel2 = list(map(int,input().split()))
tel3 = list(map(int,input().split()))
inf = int(1e10)

w = [[inf] * 8 for _ in range(8)]
w[0][1] = abs(tel1[0] - xs) + abs(tel1[1] - ys)
w[0][2] = abs(tel2[0] - xs) + abs(tel2[1] - ys)
w[0][3] = abs(tel3[0] - xs) + abs(tel3[1] - ys)
w[0][4] = abs(tel1[2] - xs) + abs(tel1[3] - ys)
w[0][5] = abs(tel2[2] - xs) + abs(tel2[3] - ys)
w[0][6] = abs(tel3[2] - xs) + abs(tel3[3] - ys)
w[1][7] = abs(tel1[0] - xe) + abs(tel1[1] - ye)
w[2][7] = abs(tel2[0] - xe) + abs(tel2[1] - ye)
w[3][7] = abs(tel3[0] - xe) + abs(tel3[1] - ye)
w[4][7] = abs(tel1[2] - xe) + abs(tel1[3] - ye)
w[5][7] = abs(tel2[2] - xe) + abs(tel2[3] - ye)
w[6][7] = abs(tel3[2] - xe) + abs(tel3[3] - ye)
w[0][7] = abs(xs - xe) + abs(ys - ye)
w[1][2] = abs(tel1[0] - tel2[0]) + abs(tel1[1] - tel2[1])
w[1][3] = abs(tel1[0] - tel3[0]) + abs(tel1[1] - tel3[1])
w[1][4] = 10
w[1][5] = abs(tel1[0] - tel2[2]) + abs(tel1[1] - tel2[3])
w[1][6] = abs(tel1[0] - tel3[2]) + abs(tel1[1] - tel3[3])
w[2][1] = w[1][2]
w[2][3] = abs(tel2[0] - tel3[0]) + abs(tel2[1] - tel3[1])
w[2][4] = abs(tel2[0] - tel1[2]) + abs(tel2[1] - tel1[3])
w[2][5] = 10
w[2][6] = abs(tel2[0] - tel3[2]) + abs(tel2[1] - tel3[3])
w[3][1] = w[1][3]
w[3][2] = w[2][3]
w[3][4] = abs(tel3[0] - tel1[2]) + abs(tel3[1] - tel1[3])
w[3][5] = abs(tel3[0] - tel2[2]) + abs(tel3[1] - tel2[3])
w[3][6] = 10
w[4][1] = w[1][4]
w[4][2] = w[2][4]
w[4][3] = w[3][4]
w[4][5] = abs(tel1[2] - tel2[2]) + abs(tel1[3] - tel2[3])
w[4][6] = abs(tel1[2] - tel3[2]) + abs(tel1[3] - tel3[3])
w[5][1] = w[1][5]
w[5][2] = w[2][5]
w[5][3] = w[3][5]
w[5][4] = w[4][5]
w[5][6] = abs(tel2[2] - tel3[2]) + abs(tel2[3] - tel3[3])
w[6][1] = w[1][6]
w[6][2] = w[2][6]
w[6][3] = w[3][6]
w[6][4] = w[4][6]
w[6][5] = w[5][6]

dist = [inf]*8
dist[0] = 0

dijk = []
heappush(dijk,(0,0))
while dijk:
    now_dist,now = heappop(dijk)
    for i in range(8):
        new_dist = now_dist+w[now][i]
        if new_dist < dist[i]:
            heappush(dijk,(new_dist,i))
            dist[i] = new_dist

print(dist[7])