# 23830: 제기차기
import sys
input = sys.stdin.readline

def solution():
    N = int(input())
    A = list(map(int, input().split()))
    S = sum(A)
    p, q, r, s = map(int, input().split())

    def calc(k):
        high = k + r
        low = k
        ret = S
        for a in A:

            if a > high: ret -= p
            elif a < low: ret += q
        if ret < s: return False
        else: return True

    st, e = 1, 100002
    while st < e:
        m = (st + e) // 2
        if calc(m):
            e = m
        else: st = m + 1
    if e == 100002: print(-1)
    else: print(e)

solution()