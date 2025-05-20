# 26586: Feed Store
import sys
input = sys.stdin.readline
inf = int(1e9)

C = int(input())
farm_input = list(map(str, input().split()))
F = 1 + len(farm_input)
farm = [0]
road_number = dict()
road_number['A'] = 0
for f in farm_input:
    road_number[f[0]] = len(farm)
    farm.append(int(f[1:]))
road = [[inf] * F for _ in range(F)]
while True:
    road_input = input().strip()
    if road_input == "": break

    u, v = road_number[road_input[0]], road_number[road_input[2]]
    w = int(road_input[4:])
    road[u][v] = min(road[u][v], w)
    road[v][u] = min(road[v][u], w)

for k in range(F):
    for i in range(F):
        for j in range(F):
            if i == j: road[i][j] = 0
            road[i][j] = min(road[i][j], road[i][k] + road[k][j])



def tsp(now, visit):

print()