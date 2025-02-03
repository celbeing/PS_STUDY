# 2825: 수업시간에 교수님 몰래 교실을 나간 상근이
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    bm = [0] * 1024
    for _ in range(n):
        bit = 0
        k = int(input())
        while k:
            bit |= 1 << (k % 10)
            k //= 10
        bm[bit] += 1
    res = 0
    for i in range(1, 1024):
        pair = 0
        for j in range(i + 1, 1024):
            if i & j:
                pair += bm[j]
        res += bm[i] * pair
        res += bm[i] * (bm[i] - 1) // 2
    print(res)
    return
solution()