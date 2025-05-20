# 23845: 마트료시카
import sys
sys.setrecursionlimit(200000)
input = sys.stdin.readline
def solution():
    n = int(input())
    size = list(map(int, input().split()))
    count = [0] * 100001
    for s in size: count[s] += 1
    def find(k, s):
        ret = 0
        e = s
        while s < 100001:
            if count[s] == k:
                s += 1
            elif count[s] > k:
                r, f = find(k + 1, s)
                ret += r
                s = f
            else:
                break
        return ret + (s - 1) * (s - e), s
    result, k = find(0, 0)
    print(result - 10000100000)
solution()