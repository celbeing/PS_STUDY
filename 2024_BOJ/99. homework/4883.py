import sys
input = sys.stdin.readline
def solution():
    tc = 0
    while True:
        tc += 1
        n = int(input())
        cost = list(map(int, input().split()))
        cost[0] = int(1e9)
        for _ in range(n - 1):
            now = list(map(int, input().split()))
            now[0] += min(cost[:2])
            now[1] += min(cost)
            now[2] += min(cost[1:])
            cost = now[:]
        print(f"{tc}. {cost[1]}")
solution()