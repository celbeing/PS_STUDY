# 13397: 구간 나누기 2
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
a = list(map(int, input().split()))

s, e = 0, 10000

def count_seg(k, a):
    count = 1
    h, l = a[0], a[0]
    for p in a:
        if p > h: h = p
        elif p < l: l = p

        if h - l > k:
            count += 1
            h, l = p, p
    return count

while s < e:
    m = (s + e) // 2
    k = count_seg(m, a)
    if k <= M: e = m
    else: s = m + 1

print(s)