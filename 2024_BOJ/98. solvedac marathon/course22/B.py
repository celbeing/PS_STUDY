#31214: НАМАЛЯВАНЕ
import sys
input = sys.stdin.readline
def solution():
    a = list(map(int, input().split()))
    k = int(input())
    s, e = 0, 1000000001
    while s < e:
        m = (s + e) // 2
        t = 0
        for n in a:
            if n > m: t += n - m
        if t > k: s = m + 1
        else: e = m
    print(s)
solution()