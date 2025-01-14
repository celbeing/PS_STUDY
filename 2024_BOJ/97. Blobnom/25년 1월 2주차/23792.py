# 23792: K번째 음식 찾기 2
import sys
input = sys.stdin.readline
def solution():
    n = int(input())
    a = [0] + list(map(int, input().split()))
    b = [0] + list(map(int, input().split()))
    c = [0] + list(map(int, input().split()))
    for _ in range(int(input())):
        x, y, z, k = map(int, input().split())
        s, e = 0, max(a[x], max(b[y], c[z]))
        while s <= e:
            m = (s + e + 1) // 2
            sa, sb, sc = 1, 1, 1
            ea, eb, ec = x, y, z
            while sa < ea:
                ma = (sa + ea + 1) // 2
                if a[ma] <= m: sa = ma
                else: ea = ma - 1
            while sb < eb:
                mb = (sb + eb + 1) // 2
                if b[mb] < m:
                    sb = mb
                else:
                    eb = mb - 1
            while sc < ec:
                mc = (sc + ec + 1) // 2
                if c[mc] < m:
                    sc = mc
                else:
                    ec = mc - 1
            if sa + sb + sc == k:
                res = max(a[sa], max(b[sb], c[sc]))
                if res == a[sa]:
                    print(1, sa)
                elif res == b[sb]:
                    print(2, sb)
                else:
                    print(3, sc)
                break
            elif sa + sb + sc < k:
                s = m
            else:
                e = m - 1
solution()