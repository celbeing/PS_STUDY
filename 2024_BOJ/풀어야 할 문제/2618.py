#2618 경찰차
import sys
input = sys.stdin.readline
N = int(input())
W = int(input())
case = [[1,1]]+[list(map(int,input().split())) for _ in range(W)]
dist = [[0 for _ in range(W+1)] for _ in range(W+1)]
for i in range(1,W+1):
    t = case[i][0] + case[i][1]
    dist[0][i] = t - 2
    dist[i][0] = N*2 - t
    for j in range(1,i):
        dist[j][i] = abs(case[i][0] - case[j][0]) + abs(case[i][1] - case[j][1])
        dist[i][j] = dist[j][i]
print("done")