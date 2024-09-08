#15513: Lottery for Vitcoins at Moloco (Hard)
import sys
input = sys.stdin.readline
def solution():
    N = int(input())
    lot = []
    for i in range(1, N + 1):
        w, q = map(int, input().split())
        lot.append((w / (10000 - q), i))
    lot.sort(key = lambda x: (-x[0], x[1]))
    result = []
    for exp, i in lot: result.append(i)
    print(*result)
solution()