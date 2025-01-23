# 9335: 소셜 광고
import sys
input = sys.stdin.readline
def solution():
    def bf(d, dep, now, t, i):
        if dep == d:
            return 1 if len(now) == t else 0

        for k in range(i + 1, n + 1 - d + dep):
            next = set()
            next.update(now)
            next.update(f[k])
            res = bf(d, dep + 1, next, t, k)
            if res: return 1
        return 0

    for _ in range(int(input())):
        n = int(input())
        f = [[]]
        for i in range(1, n + 1):
            f.append([i] + list(map(int, input().split()))[1:])
        for i in range(1, n + 1):
            now = set()
            if bf(i, 0, now, n, 0):
                print(i)
                break
solution()