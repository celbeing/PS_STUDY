# 19780: Мерлин
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    a = sorted(list(map(int, input().split())))
    prefix_sum = [0] * n
    need = [0] * n
    prefix_sum[0] = a[0]
    for i in range(1, n):
        prefix_sum[i] = a[i] + prefix_sum[i - 1]
        need[i] = a[i] * (i + 1) - prefix_sum[i]
    s = 0
    res = 0
    for i in range(n - 1, 0, -1):
        if need[i] <= s: break
        s += a[i]
        res += 1
    print(res)
solution()