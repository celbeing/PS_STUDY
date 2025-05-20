# 2201: 이친수 찾기
import sys
input = sys.stdin.readline
def solution():
    k = int(input())
    dp = [0, 1, 1]
    pr = [0, 1, 2]
    for i in range(84):
        dp.append(1 + pr[-2])
        pr.append(pr[-1] + dp[-1])
    res = 0
    while k:
        t = 1
        c = 1
        while k > pr[c]:
            t <<= 1
            c += 1
        k -= pr[c - 1] + 1
        res ^= t
    print(bin(res)[2:])
solution()