# 12723: Minimum Scalar Product (Small)
import sys
input = sys.stdin.readline
def solution():
    for i in range(1, int(input()) + 1):
        n = int(input())
        v = sorted(list(map(int, input().split())))
        w = sorted(list(map(int, input().split())), reverse = True)
        res = 0
        for j in range(n):
            res += v[j] * w[j]
        print(f'Case #{i}: {res}')
solution()