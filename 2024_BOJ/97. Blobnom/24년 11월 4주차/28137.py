# 28137: 뭐라고? 안들려
import sys
input = sys.stdin.readline
def solution():
    N, K = map(int, input().split())
    y_inter = set()
    count = dict()
    for _ in range(N):
        x, y = map(int, input().split())
        k = y - x * K
        if k in y_inter:
            count[k] += 1
        else:
            count[k] = 0
            y_inter.add(k)
    res = 0
    for k in list(y_inter):
        if count[k]:
           res += count[k] * (count[k] + 1)
    print(res)
solution()