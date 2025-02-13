import sys
input = sys.stdin.readline
def solution():
    tc = 0
    while True:
        tc += 1
        n = int(input())
        cost = [[],[]]
        cost[0] = list(map(int, input().split()))
        cost[0][0] = int(1e9)
        for _ in range(n - 1):
            cost[1] = list(map(int, input().split()))
            now = [int(1e9)] * 3
            now[0] = min(cost[:2]) + cost[1][0]
            now[1] = min(min(cost), now[0]) + cost[1][1]
            now[2] = min(min(cost[1:]), now[1]) + cost[1][2]
            cost[0] = now[:]
        print(f"{tc}. {cost[0][1]}")
solution()